"""
Bot Vision Suite - Configuration

Este módulo gerencia a configuração da biblioteca, incluindo detecção automática
do Tesseract e configurações específicas do sistema operacional.
"""

import os
import sys
import shutil
import platform
import logging
from pathlib import Path
from typing import Optional, Dict, Any

from ..exceptions import TesseractNotFoundError, ConfigurationError

logger = logging.getLogger(__name__)


class BotVisionConfig:
    """
    Classe de configuração principal do Bot Vision Suite.
    
    Gerencia automaticamente:
    - Detecção do Tesseract OCR
    - Configurações específicas do OS
    - Validação de dependências
    - Configurações padrão
    """
    
    def __init__(self, config_dict: Optional[Dict[str, Any]] = None):
        """
        Inicializa a configuração.
        
        Args:
            config_dict (dict, optional): Dicionário de configurações customizadas
        """
        self.config = self._load_default_config()
        
        if config_dict:
            self.config.update(config_dict)
        
        self._detect_tesseract()
        self._validate_dependencies()
        self._validate_overlay_config()
        self._validate_mouse_button_config()
    
    def _validate_overlay_config(self) -> None:
        """Valida configurações do overlay."""
        valid_colors = [
            "red", "blue", "green", "yellow", 
            "purple", "orange", "cyan", "magenta", 
            "white", "black"
        ]
        
        overlay_color = self.config.get("overlay_color", "red")
        if overlay_color not in valid_colors:
            logger.warning(f"Cor de overlay inválida '{overlay_color}'. Usando 'red'. "
                         f"Cores válidas: {', '.join(valid_colors)}")
            self.config["overlay_color"] = "red"
        
        # Validar duração
        overlay_duration = self.config.get("overlay_duration", 1000)
        if not isinstance(overlay_duration, (int, float)) or overlay_duration <= 0:
            logger.warning(f"Duração de overlay inválida '{overlay_duration}'. Usando 1000ms.")
            self.config["overlay_duration"] = 1000
        
        # Validar largura
        overlay_width = self.config.get("overlay_width", 4)
        if not isinstance(overlay_width, (int, float)) or overlay_width <= 0:
            logger.warning(f"Largura de overlay inválida '{overlay_width}'. Usando 4.")
            self.config["overlay_width"] = 4
    
    def _validate_mouse_button_config(self) -> None:
        """Valida configurações de mouse_button."""
        valid_mouse_buttons = [
            "left", "right", "double", "move_to"
        ]
        
        default_mouse_button = self.config.get("default_mouse_button", "left")
        if default_mouse_button not in valid_mouse_buttons:
            logger.warning(f"Botão do mouse padrão inválido '{default_mouse_button}'. Usando 'left'. "
                         f"Opções válidas: {', '.join(valid_mouse_buttons)}")
            self.config["default_mouse_button"] = "left"
    
    def _load_default_config(self) -> Dict[str, Any]:
        """Carrega configurações padrão."""
        return {
            "tesseract_path": None,
            "tesseract_data_path": None,
            "confidence_threshold": 75.0,
            "retry_attempts": 3,
            "default_delay": 1.0,
            "overlay_duration": 1000,
            "overlay_color": "red",  # red, blue, green, yellow, purple, orange, cyan, magenta, white
            "overlay_width": 4,
            "show_overlay": True,  # Controla se exibe overlay visual antes do clique
            "overlay_enabled": True,  # Controla se o sistema de overlay está ativo
            "default_mouse_button": "left",  # Botão padrão do mouse: 'left', 'right', 'double', 'move_to'
            "log_level": "INFO",
            "ocr_languages": ["eng"],
            "image_processing_methods": "all",  # ou lista específica
            "click_duration": 0.1,
            "movement_duration": 0.1,
            # 🆕 NOVOS PARÂMETROS v1.3.0+
            "use_virtual_mouse": False,  # Mouse virtual (cursor não move)
            "wait_timeout": 30,  # Timeout global para wait parameters (30-300s)
            "screenshot_delay": 0.1,  # Delay para captura de tela
        }
    
    def _detect_tesseract(self) -> None:
        """
        Detecta automaticamente a instalação do Tesseract no sistema.
        """
        tesseract_paths = self._get_tesseract_paths()
        
        for path in tesseract_paths:
            if self._validate_tesseract_path(path):
                self.config["tesseract_path"] = path
                self.config["tesseract_data_path"] = self._get_tessdata_path(path)
                logger.info(f"Tesseract encontrado em: {path}")
                return
        
        # Se não encontrou, tenta usar o do PATH
        tesseract_cmd = shutil.which("tesseract")
        if tesseract_cmd and self._validate_tesseract_path(tesseract_cmd):
            self.config["tesseract_path"] = tesseract_cmd
            logger.info(f"Tesseract encontrado no PATH: {tesseract_cmd}")
            return
        
        # Se chegou aqui, não encontrou o Tesseract
        logger.error("Tesseract OCR não encontrado no sistema")
        raise TesseractNotFoundError(
            "Tesseract OCR não foi encontrado. Por favor, instale o Tesseract OCR:\n"
            "Windows: https://github.com/UB-Mannheim/tesseract/wiki\n"
            "Linux: sudo apt-get install tesseract-ocr\n"
            "macOS: brew install tesseract"
        )
    
    def _get_tesseract_paths(self) -> list:
        """Retorna lista de possíveis caminhos do Tesseract baseado no OS."""
        system = platform.system().lower()
        
        if system == "windows":
            return [
                r"C:\Program Files\Tesseract-OCR\tesseract.exe",
                r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
                r"C:\Users\{}\AppData\Local\Tesseract-OCR\tesseract.exe".format(os.getenv("USERNAME", "")),
                r"C:\Program Files\Tesseract-OCR\tesseract.exe",
                r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            ]
        elif system == "linux":
            return [
                "/usr/bin/tesseract",
                "/usr/local/bin/tesseract",
                "/opt/tesseract/bin/tesseract",
                "/snap/bin/tesseract",
            ]
        elif system == "darwin":  # macOS
            return [
                "/usr/local/bin/tesseract",
                "/opt/homebrew/bin/tesseract",
                "/usr/bin/tesseract",
                "/Applications/Tesseract.app/Contents/MacOS/tesseract",
            ]
        else:
            return ["/usr/bin/tesseract", "/usr/local/bin/tesseract"]
    
    def _validate_tesseract_path(self, path: str) -> bool:
        """Valida se um caminho do Tesseract é válido."""
        if not path or not os.path.exists(path):
            return False
        
        try:
            import subprocess
            result = subprocess.run([path, "--version"], 
                                  capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Erro ao validar Tesseract em {path}: {e}")
            return False
    
    def _get_tessdata_path(self, tesseract_path: str) -> Optional[str]:
        """Determina o caminho do tessdata baseado no caminho do Tesseract."""
        tesseract_dir = os.path.dirname(tesseract_path)
        
        # Possíveis localizações do tessdata
        possible_paths = [
            os.path.join(tesseract_dir, "tessdata"),
            os.path.join(os.path.dirname(tesseract_dir), "tessdata"),
            os.path.join(tesseract_dir, "..", "share", "tessdata"),
            "/usr/share/tesseract-ocr/5/tessdata",  # Linux
            "/usr/share/tesseract-ocr/4/tessdata",  # Linux
            "/usr/local/share/tessdata",  # macOS
        ]
        
        for path in possible_paths:
            if os.path.exists(path) and os.path.isdir(path):
                return path
        
        logger.warning("Não foi possível determinar o caminho do tessdata")
        return None
    
    def _validate_dependencies(self) -> None:
        """Valida se todas as dependências estão instaladas."""
        required_modules = [
            "pyautogui",
            "pytesseract", 
            "cv2",
            "PIL",
            "numpy",
            "pyperclip"
        ]
        
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)
        
        if missing_modules:
            raise ConfigurationError(
                f"Módulos necessários não encontrados: {', '.join(missing_modules)}\n"
                f"Execute: pip install bot-vision-suite[dev]"
            )
    
    def setup_tesseract(self) -> None:
        """Configura o Tesseract com as configurações atuais."""
        try:
            import pytesseract
            
            if self.config["tesseract_path"]:
                pytesseract.pytesseract.tesseract_cmd = self.config["tesseract_path"]
            
            if self.config["tesseract_data_path"]:
                os.environ['TESSDATA_PREFIX'] = self.config["tesseract_data_path"]
            
            logger.info("Tesseract configurado com sucesso")
            
        except ImportError:
            raise ConfigurationError("pytesseract não está instalado")
    
    def setup_logging(self) -> None:
        """Configura o sistema de logging."""
        log_level = getattr(logging, self.config["log_level"].upper(), logging.INFO)
        logging.basicConfig(
            level=log_level,
            format="[%(levelname)s] %(name)s: %(message)s"
        )
    
    def __getattr__(self, name):
        """Permite acesso direto aos valores de configuração como atributos."""
        if name == 'config':
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        if hasattr(self, 'config') and name in self.config:
            return self.config[name]
        raise AttributeError(f"Configuração '{name}' não encontrada")
    
    def __setattr__(self, name, value):
        """Permite definir valores de configuração como atributos."""
        if name in ['config'] or not hasattr(self, 'config'):
            super().__setattr__(name, value)
        elif name in self.config:
            self.config[name] = value
        else:
            super().__setattr__(name, value)
    
    def get(self, key, default=None):
        """Obtém valor de configuração com valor padrão."""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Define valor de configuração."""
        self.config[key] = value
    
    def update(self, config_dict):
        """Atualiza múltiplas configurações."""
        self.config.update(config_dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Retorna todas as configurações como dicionário."""
        return self.config.copy()
    

def create_config_from_file(config_path: str) -> BotVisionConfig:
    """
    Cria configuração a partir de arquivo.
    
    Args:
        config_path (str): Caminho para arquivo de configuração (JSON ou YAML)
    
    Returns:
        BotVisionConfig: Instância configurada
    """
    config_path = Path(config_path)
    
    if not config_path.exists():
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {config_path}")
    
    if config_path.suffix.lower() == '.json':
        import json
        with open(config_path, 'r', encoding='utf-8') as f:
            config_dict = json.load(f)
    elif config_path.suffix.lower() in ['.yml', '.yaml']:
        try:
            import yaml
            with open(config_path, 'r', encoding='utf-8') as f:
                config_dict = yaml.safe_load(f)
        except ImportError:
            raise ConfigurationError("PyYAML não está instalado. Execute: pip install PyYAML")
    else:
        raise ConfigurationError(f"Formato de arquivo não suportado: {config_path.suffix}")
    
    return BotVisionConfig(config_dict)


# Instância global padrão
default_config = None

def get_default_config() -> BotVisionConfig:
    """Retorna a instância de configuração padrão (singleton)."""
    global default_config
    if default_config is None:
        default_config = BotVisionConfig()
    return default_config
