from AOT_biomaps.Config import config

import numba
import torch
import numpy as np
import os
from tqdm import trange


def _LS_GPU_basic(SMatrix, y, numIterations, isSavingEachIteration, withTumor):
    """
    Least Squares using GPU — fully flattened variables, corrected dimensions.
    """
    try:
        device = torch.device(f"cuda:{config.select_best_gpu()}")
        T, Z, X, N = SMatrix.shape
        ZX = Z * X
        TN = T * N

        # Vérification des dimensions de y
        if y.shape != (T, N):
            raise ValueError(f"Expected y shape: ({T}, {N}), got {y.shape}")

        # Conversion en tenseurs GPU
        A_flat = torch.from_numpy(SMatrix).to(device=device, dtype=torch.float32).permute(0, 3, 1, 2).reshape(TN, ZX)
        y_flat = torch.from_numpy(y).to(device=device, dtype=torch.float32).reshape(TN)  # TN éléments

        # Initialisation de theta
        theta_flat = torch.zeros(ZX, dtype=torch.float32, device=device)

        # Normalisation pour conditionnement
        A_normalized = A_flat / (torch.norm(A_flat, dim=0, keepdim=True) + 1e-8)
        y_normalized = y_flat / (torch.norm(y_flat) + 1e-8)

        description = f"AOT-BioMaps -- LS Reconstruction ---- {'WITH' if withTumor else 'WITHOUT'} TUMOR ---- GPU {torch.cuda.current_device()}"
        if isSavingEachIteration:
            matrix_theta_torch = [theta_flat.reshape(Z, X).clone()]

        # Méthode des moindres carrés (gradient conjugué)
        with torch.no_grad():
            for _ in trange(numIterations, desc=description):
                # Calcul du résidu: r = y - A*theta
                r = y_normalized - A_normalized @ theta_flat
                p = r.clone()
                rsold = torch.dot(r, r)

                # Itérations du gradient conjugué
                for _ in range(2):  # 2 itérations internes
                    Ap = A_normalized @ p
                    alpha = rsold / (torch.dot(p, Ap) + 1e-8)
                    theta_flat += alpha * p
                    r -= alpha * Ap
                    rsnew = torch.dot(r, r)
                    if rsnew < 1e-8:
                        break
                    p = r + (rsnew / rsold) * p
                    rsold = rsnew

                if isSavingEachIteration:
                    matrix_theta_torch.append(theta_flat.reshape(Z, X).clone())

        # Libération mémoire
        del A_flat, y_flat, A_normalized, y_normalized
        torch.cuda.empty_cache()

        if isSavingEachIteration:
            return [theta.reshape(Z, X).cpu().numpy() for theta in matrix_theta_torch]
        else:
            return theta_flat.reshape(Z, X).cpu().numpy()

    except Exception as e:
        print("Error in LS GPU basic:", type(e).__name__, ":", e)
        torch.cuda.empty_cache()
        return None

def _LS_CPU_basic(SMatrix, y, numIterations, isSavingEachIteration, withTumor):
    try:
        T, Z, X, N = SMatrix.shape
        theta_p = np.ones((Z, X))
        matrix_theta = [theta_p.copy()]

        description = f"AOT-BioMaps -- LS Reconstruction ---- {'WITH' if withTumor else 'WITHOUT'} TUMOR ---- CPU (basic) ----"

        for _ in trange(numIterations, desc=description):
            # Calcul de A^T A et A^T y
            ATA = np.zeros((Z, X, Z, X))
            ATy = np.zeros((Z, X))
            for _t in range(T):
                for _n in range(N):
                    ATA += np.einsum('ij,kl->ijkl', SMatrix[_t, :, :, _n], SMatrix[_t, :, :, _n])
                    ATy += SMatrix[_t, :, :, _n] * y[_t, _n]

            # Résolution du système linéaire (simplifiée)
            theta_p = np.linalg.solve(ATA.reshape(Z*X, Z*X), ATy.reshape(Z*X)).reshape(Z, X)
            matrix_theta.append(theta_p.copy())

        if not isSavingEachIteration:
            return matrix_theta[-1]
        else:
            return matrix_theta

    except Exception as e:
        print("Error in basic CPU LS:", type(e).__name__, ":", e)
        return None

def _LS_CPU_opti(SMatrix, y, numIterations, isSavingEachIteration, withTumor):
    try:
        T, Z, X, N = SMatrix.shape
        A_flat = SMatrix.astype(np.float32).transpose(0, 3, 1, 2).reshape(T*N, Z*X)
        y_flat = y.astype(np.float32).reshape(-1)

        # Initialisation
        theta_flat = np.zeros(Z*X, dtype=np.float32)
        matrix_theta = [theta_flat.reshape(Z, X).copy()]

        # Normalisation
        A_normalized = A_flat / (np.linalg.norm(A_flat, axis=0, keepdims=True) + 1e-8)
        y_normalized = y_flat / (np.linalg.norm(y_flat) + 1e-8)

        description = f"AOT-BioMaps -- LS Reconstruction ---- {'WITH' if withTumor else 'WITHOUT'} TUMOR ---- CPU (optimized) ----"

        for _ in trange(numIterations, desc=description):
            # Méthode des moindres carrés (équation normale)
            ATA = A_normalized.T @ A_normalized
            ATy = A_normalized.T @ y_normalized
            theta_flat = np.linalg.lstsq(ATA, ATy, rcond=None)[0]
            matrix_theta.append(theta_flat.reshape(Z, X).copy())

        if not isSavingEachIteration:
            return matrix_theta[-1]
        else:
            return matrix_theta

    except Exception as e:
        print("Error in optimized CPU LS:", type(e).__name__, ":", e)
        return None

def _LS_GPU_multi(SMatrix, y, numIterations, isSavingEachIteration, withTumor):
    try:
        num_gpus = torch.cuda.device_count()
        device = torch.device('cuda:0')
        T, Z, X, N = SMatrix.shape

        # Conversion en tenseurs
        A_matrix_torch = torch.tensor(SMatrix, dtype=torch.float32).to(device).permute(0, 3, 1, 2).reshape(T*N, Z*X)
        y_torch = torch.tensor(y, dtype=torch.float32).to(device).reshape(-1)

        # Partitionnement des données
        A_split = torch.chunk(A_matrix_torch, num_gpus, dim=0)
        y_split = torch.chunk(y_torch, num_gpus)

        # Initialisation
        theta_0 = torch.zeros(Z*X, dtype=torch.float32, device=device)
        theta_list = [theta_0.clone().to(device) for _ in range(num_gpus)]

        description = f"AOT-BioMaps -- LS Reconstruction ---- {'WITH' if withTumor else 'WITHOUT'} TUMOR ---- multi-GPU ----"

        for _ in trange(numIterations, desc=description):
            # Gradient conjugué distribué
            for i in range(num_gpus):
                with torch.cuda.device(f'cuda:{i}'):
                    A_i = A_split[i].to(f'cuda:{i}')
                    y_i = y_split[i].to(f'cuda:{i}')
                    theta_p = theta_list[i].to(f'cuda:{i}')

                    r = y_i - A_i @ theta_p
                    p = r.clone()
                    rsold = torch.dot(r, r)

                    for _ in range(2):  # 2 itérations internes
                        Ap = A_i @ p
                        alpha = rsold / (torch.dot(p, Ap) + 1e-8)
                        theta_p += alpha * p
                        r -= alpha * Ap
                        rsnew = torch.dot(r, r)
                        if rsnew < 1e-8:
                            break
                        p = r + (rsnew / rsold) * p
                        rsold = rsnew

                    theta_list[i] = theta_p.to('cuda:0')

        # Libération mémoire
        del A_matrix_torch, y_torch, A_split, y_split, theta_0
        torch.cuda.empty_cache()
        for i in range(num_gpus):
            torch.cuda.empty_cache()

        if not isSavingEachIteration:
            return torch.stack(theta_list).mean(dim=0).cpu().numpy()
        else:
            return [theta.cpu().numpy() for theta in theta_list]

    except Exception as e:
        print("Error in multi-GPU LS:", type(e).__name__, ":", e)
        del A_matrix_torch, y_torch, A_split, y_split, theta_0
        torch.cuda.empty_cache()
        for i in range(num_gpus):
            torch.cuda.empty_cache()
        return None
