import os
import warnings
import torch
import ctypes
import platform

# ACOUSTIC
from .AOT_Acoustic._mainAcoustic import *
from .AOT_Acoustic.AcousticEnums import *
from .AOT_Acoustic.AcousticTools import *
from .AOT_Acoustic.FocusedWave import *
from .AOT_Acoustic.IrregularWave import *
from .AOT_Acoustic.PlaneWave import *
from .AOT_Acoustic.StructuredWave import *
# EXPERIMENT
from .AOT_Experiment._mainExperiment import *
from .AOT_Experiment.Focus import *
from .AOT_Experiment.Tomography import *
# OPTIC
from .AOT_Optic._mainOptic import *
from .AOT_Optic.Absorber import *
from .AOT_Optic.Laser import *
from .AOT_Optic.OpticEnums import *
# RECONSTRUCTION
from .AOT_Recon._mainRecon import *
from .AOT_Recon.AlgebraicRecon import *
from .AOT_Recon.AnalyticRecon import *
from .AOT_Recon.BayesianRecon import *
from .AOT_Recon.DeepLearningRecon import *
from .AOT_Recon.PrimalDualRecon import *
from .AOT_Recon.ReconEnums import *
from .AOT_Recon.ReconTools import *
# OPTIMIZERS
from .AOT_Recon.AOT_Optimizers.DEPIERRO import *
from .AOT_Recon.AOT_Optimizers.MAPEM import *
from .AOT_Recon.AOT_Optimizers.MLEM import *
from .AOT_Recon.AOT_Optimizers.PDHG import *
# POTENTIAL FUNCTIONS
from .AOT_Recon.AOT_PotentialFunctions.Huber import *
from .AOT_Recon.AOT_PotentialFunctions.Quadratic import *
from .AOT_Recon.AOT_PotentialFunctions.RelativeDifferences import *
# CONFIG AND SETTINGS
from .Config import config
from .Settings import *

__version__ = '2.9.74'
__process__ = config.get_process()

def initialize(process=None):
    """
    Initialise ou modifie le backend de calcul (GPU/CPU) et configure l'environnement pour les bibliothèques partagées.
    Args:
        process (str, optional): 'gpu' pour forcer le GPU, 'cpu' pour forcer le CPU.
    Raises:
        RuntimeError: Si CONDA_PREFIX n'est pas défini ou si libsz.so.2 est introuvable.
    """
    global __process__

    # 1. Vérifie que CONDA_PREFIX est défini
    conda_prefix = os.environ.get('CONDA_PREFIX', '')
    if not conda_prefix:
        raise RuntimeError("CONDA_PREFIX not set. Activate your Conda environment first.")

    # 2. Détermine le chemin de libsz.so.2 selon l'OS
    if platform.system() == 'Windows':
        libsz_name = 'libsz.dll'
        env_var = 'PATH'
        lib_path = os.path.join(conda_prefix, 'Library', 'bin')
    else:  # Linux/Mac
        libsz_name = 'libsz.so.2'
        env_var = 'LD_LIBRARY_PATH'
        lib_path = os.path.join(conda_prefix, 'lib')

    # 3. Vérifie que le fichier existe
    libsz_path = os.path.join(lib_path, libsz_name)
    if not os.path.exists(libsz_path):
        raise RuntimeError(
            f"{libsz_name} not found at {libsz_path}. "
            f"Install it with: conda install -c conda-forge libaec"
        )

    # 4. Charge la bibliothèque pour le processus courant
    try:
        ctypes.CDLL(libsz_path, mode=ctypes.RTLD_GLOBAL)
    except OSError as e:
        raise RuntimeError(f"Failed to load {libsz_name}: {e}")

    # 5. Met à jour LD_LIBRARY_PATH pour le processus courant ET les sous-processus
    if env_var in os.environ:
        os.environ[env_var] = f"{lib_path}{os.pathsep}{os.environ[env_var]}"
    else:
        os.environ[env_var] = lib_path

    # 6. Force la transmission de LD_LIBRARY_PATH aux sous-processus
    #    en remplaçant la fonction subprocess.run si nécessaire
    original_run = subprocess.run

    def run_with_updated_env(*args, **kwargs):
        env = kwargs.pop('env', os.environ.copy())
        env[env_var] = lib_path + os.pathsep + env.get(env_var, '')
        return original_run(*args, env=env, **kwargs)

    subprocess.run = run_with_updated_env

    # 7. Vérifie la disponibilité du GPU si demandé
    if process is not None:
        if process not in ['cpu', 'gpu']:
            raise ValueError("process must be 'cpu' or 'gpu'")
        config.set_process(process)
        __process__ = process

    if __process__ == 'gpu':
        try:
            if not torch.cuda.is_available():
                warnings.warn("GPU requested but PyTorch cannot access it. Falling back to CPU.", UserWarning)
                config.set_process('cpu')
                __process__ = 'cpu'
        except Exception as e:
            warnings.warn(f"PyTorch GPU check failed: {e}. Falling back to CPU.", UserWarning)
            config.set_process('cpu')
            __process__ = 'cpu'

    return __process__



