from AOT_biomaps.Config import config
import numba
import torch
import numpy as np
import os
from tqdm import trange

def _LS_GPU_basic(SMatrix, y, numIterations, isSavingEachIteration, withTumor):
    try:
        device = torch.device(f"cuda:{config.select_best_gpu()}")
        T, Z, X, N = SMatrix.shape
        ZX = Z * X
        TN = T * N
        if y.shape != (T, N):
            raise ValueError(f"Expected y shape: ({T}, {N}), got {y.shape}")

        A_flat = torch.from_numpy(SMatrix).to(device=device, dtype=torch.float32).permute(0, 3, 1, 2).reshape(TN, ZX)
        y_flat = torch.from_numpy(y).to(device=device, dtype=torch.float32).reshape(TN)
        theta_flat = torch.zeros(ZX, dtype=torch.float32, device=device)

        matrix_theta_torch = []
        if isSavingEachIteration:
            matrix_theta_torch.append(theta_flat.reshape(Z, X).clone())

        col_norms = torch.norm(A_flat, dim=0, keepdim=True)
        A_normalized = A_flat / (col_norms + 1e-8)
        y_normalized = y_flat / (torch.norm(y_flat) + 1e-8)

        description = f"AOT-BioMaps -- LS Reconstruction ---- {'WITH' if withTumor else 'WITHOUT'} TUMOR ---- GPU {torch.cuda.current_device()}"
        with torch.no_grad():
            for k in trange(numIterations, desc=description):
                r = y_normalized - A_normalized @ theta_flat
                p = r.clone()
                rsold = torch.dot(r, r)
                for _ in range(2):
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

        del A_flat, y_flat, A_normalized, y_normalized
        torch.cuda.empty_cache()

        if isSavingEachIteration:
            return [theta.cpu().numpy() for theta in matrix_theta_torch]
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
        matrix_theta = []
        if isSavingEachIteration:
            matrix_theta.append(theta_p.copy())

        description = f"AOT-BioMaps -- LS Reconstruction ---- {'WITH' if withTumor else 'WITHOUT'} TUMOR ---- CPU (basic) ----"
        for k in trange(numIterations, desc=description):
            ATA = np.zeros((Z, X, Z, X))
            ATy = np.zeros((Z, X))
            for _t in range(T):
                for _n in range(N):
                    ATA += np.einsum('ij,kl->ijkl', SMatrix[_t, :, :, _n], SMatrix[_t, :, :, _n])
                    ATy += SMatrix[_t, :, :, _n] * y[_t, _n]
            theta_p = np.linalg.solve(ATA.reshape(Z*X, Z*X), ATy.reshape(Z*X)).reshape(Z, X)

            if isSavingEachIteration:
                matrix_theta.append(theta_p.copy())

        if isSavingEachIteration:
            return matrix_theta
        else:
            return theta_p

    except Exception as e:
        print("Error in basic CPU LS:", type(e).__name__, ":", e)
        return None

def _LS_CPU_opti(SMatrix, y, numIterations, isSavingEachIteration, withTumor):
    try:
        T, Z, X, N = SMatrix.shape
        A_flat = SMatrix.astype(np.float32).transpose(0, 3, 1, 2).reshape(T*N, Z*X)
        y_flat = y.astype(np.float32).reshape(-1)
        theta_flat = np.zeros(Z*X, dtype=np.float32)
        matrix_theta = []
        if isSavingEachIteration:
            matrix_theta.append(theta_flat.reshape(Z, X).copy())

        A_normalized = A_flat / (np.linalg.norm(A_flat, axis=0, keepdims=True) + 1e-8)
        y_normalized = y_flat / (np.linalg.norm(y_flat) + 1e-8)

        description = f"AOT-BioMaps -- LS Reconstruction ---- {'WITH' if withTumor else 'WITHOUT'} TUMOR ---- CPU (optimized) ----"
        for k in trange(numIterations, desc=description):
            ATA = A_normalized.T @ A_normalized
            ATy = A_normalized.T @ y_normalized
            theta_flat = np.linalg.lstsq(ATA, ATy, rcond=None)[0]

            if isSavingEachIteration:
                matrix_theta.append(theta_flat.reshape(Z, X).copy())

        if isSavingEachIteration:
            return matrix_theta
        else:
            return theta_flat.reshape(Z, X)

    except Exception as e:
        print("Error in optimized CPU LS:", type(e).__name__, ":", e)
        return None

def _LS_GPU_multi(SMatrix, y, numIterations, isSavingEachIteration, withTumor):
    try:
        num_gpus = torch.cuda.device_count()
        device = torch.device('cuda:0')
        T, Z, X, N = SMatrix.shape

        A_matrix_torch = torch.tensor(SMatrix, dtype=torch.float32).to(device).permute(0, 3, 1, 2).reshape(T*N, Z*X)
        y_torch = torch.tensor(y, dtype=torch.float32).to(device).reshape(-1)
        matrix_theta = []
        if isSavingEachIteration:
            matrix_theta.append(torch.zeros(Z, X, device=device).cpu().numpy())

        A_split = torch.chunk(A_matrix_torch, num_gpus, dim=0)
        y_split = torch.chunk(y_torch, num_gpus)
        theta_0 = torch.zeros(Z*X, dtype=torch.float32, device=device)
        theta_list = [theta_0.clone().to(device) for _ in range(num_gpus)]

        description = f"AOT-BioMaps -- LS Reconstruction ---- {'WITH' if withTumor else 'WITHOUT'} TUMOR ---- multi-GPU ----"
        for k in trange(numIterations, desc=description):
            for i in range(num_gpus):
                with torch.cuda.device(f'cuda:{i}'):
                    A_i = A_split[i].to(f'cuda:{i}')
                    y_i = y_split[i].to(f'cuda:{i}')
                    theta_p = theta_list[i].to(f'cuda:{i}')
                    r = y_i - A_i @ theta_p
                    p = r.clone()
                    rsold = torch.dot(r, r)
                    for _ in range(2):
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

            if isSavingEachIteration:
                matrix_theta.append(torch.stack(theta_list).mean(dim=0).reshape(Z, X).cpu().numpy())

        del A_matrix_torch, y_torch, A_split, y_split, theta_0
        torch.cuda.empty_cache()
        for i in range(num_gpus):
            torch.cuda.empty_cache()

        if isSavingEachIteration:
            return matrix_theta
        else:
            return torch.stack(theta_list).mean(dim=0).reshape(Z, X).cpu().numpy()

    except Exception as e:
        print("Error in multi-GPU LS:", type(e).__name__, ":", e)
        del A_matrix_torch, y_torch, A_split, y_split, theta_0
        torch.cuda.empty_cache()
        for i in range(num_gpus):
            torch.cuda.empty_cache()
        return None

def _LS_TV_GPU(SMatrix, y, numIterations, isSavingEachIteration, withTumor, lambda_tv=1e-3, L_Factor=1.0):
    device = torch.device(f"cuda:{torch.cuda.current_device()}")
    T, Z, X, N = SMatrix.shape
    A_flat = torch.from_numpy(SMatrix).to(device=device, dtype=torch.float32).permute(0, 3, 1, 2).reshape(T*N, Z*X)
    y_flat = torch.from_numpy(y).to(device=device, dtype=torch.float32).reshape(T*N)

    if torch.isnan(A_flat).any() or torch.isinf(A_flat).any():
        raise ValueError("SMatrix contient des NaN ou Inf.")
    if torch.isnan(y_flat).any() or torch.isinf(y_flat).any():
        raise ValueError("y contient des NaN ou Inf.")

    A_norm = torch.max(torch.abs(A_flat))
    y_norm = torch.max(torch.abs(y_flat))
    if A_norm > 0:
        A_flat = A_flat / A_norm
    if y_norm > 0:
        y_flat = y_flat / y_norm

    theta_flat = torch.zeros(Z*X, device=device)
    theta_prev = theta_flat.clone()
    t = torch.tensor(1.0, device=device)
    L = L_Factor * (torch.norm(A_flat, 2).item() ** 2)
    theta_history = []
    if isSavingEachIteration:
        theta_history.append(theta_flat.reshape(Z, X).clone())

    description = f"AOT-BioMaps -- LS + TV (lambda : {lambda_tv}) Reconstruction ---- {'WITH' if withTumor else 'WITHOUT'} TUMOR ---- GPU {torch.cuda.current_device()}"
    for k in trange(numIterations, desc=description):
        grad = A_flat.T @ (A_flat @ theta_flat - y_flat)
        theta_2d = theta_flat.reshape(Z, X)
        grad_tv = torch.zeros_like(theta_2d)
        grad_tv[:-1, :] += theta_2d[1:, :] - theta_2d[:-1, :]
        grad_tv[:, :-1] += theta_2d[:, 1:] - theta_2d[:, :-1]
        grad_tv = grad_tv.reshape(Z*X)
        grad_total = grad + lambda_tv * grad_tv

        theta_new = theta_flat - (1/L) * grad_total
        theta_new = torch.clamp(theta_new, min=0.0)

        t_new = (1 + torch.sqrt(1 + 4 * t**2)) / 2
        theta_flat = theta_new + ((t - 1) / t_new) * (theta_new - theta_prev)
        theta_prev = theta_new.clone()
        t = t_new

        if isSavingEachIteration:
            theta_history.append(theta_flat.reshape(Z, X).clone())

    if A_norm > 0 and y_norm > 0:
        theta_flat = theta_flat * (y_norm / (A_norm + 1e-8))

    if isSavingEachIteration:
        return [t.cpu().numpy() for t in theta_history]
    else:
        return theta_flat.reshape(Z, X).cpu().numpy()
