"""
Bot Vision Suite - Wait Manager

Este módulo implementa funcionalidades de espera inteligente para imagens,
incluindo wait_until_found e wait_until_disappears com timeout configurável.
"""

import time
import logging
from typing import Optional, Callable, Any, Tuple
from ..utils.config import BotVisionConfig

logger = logging.getLogger(__name__)


class WaitManager:
    """
    Gerenciador de operações de espera inteligente para imagens e textos.
    """

    def __init__(self, config: Optional[BotVisionConfig] = None):
        """
        Inicializa o gerenciador de espera.

        Args:
            config (BotVisionConfig, optional): Configuração da biblioteca
        """
        from ..utils.config import get_default_config
        self.config = config or get_default_config()

    def wait_until_found(self,
                        search_function: Callable[[], Any],
                        timeout: Optional[int] = None,
                        check_interval: float = 0.5,
                        description: str = "elemento") -> Any:
        """
        Aguarda até que um elemento seja encontrado.

        Args:
            search_function (Callable): Função de busca que retorna o elemento ou None
            timeout (int, optional): Timeout em segundos. Se None, usa configuração global
            check_interval (float): Intervalo entre verificações em segundos
            description (str): Descrição do elemento para logs

        Returns:
            Any: Resultado da função de busca quando encontrado, ou None se timeout

        Example:
            >>> def search_image():
            ...     return bot.find_image('button.png')
            >>>
            >>> result = wait_manager.wait_until_found(search_image, timeout=30)
        """
        timeout = timeout or self.config.get('wait_timeout', 30)
        start_time = time.time()

        logger.debug(f"Aguardando {description} aparecer (timeout: {timeout}s)")

        while (time.time() - start_time) < timeout:
            try:
                result = search_function()
                if result:
                    elapsed = time.time() - start_time
                    logger.debug(f"{description} encontrado após {elapsed:.1f}s")
                    return result

            except Exception as e:
                logger.debug(f"Erro durante busca de {description}: {e}")

            time.sleep(check_interval)

        elapsed = time.time() - start_time
        logger.debug(f"Timeout atingido para {description} após {elapsed:.1f}s")
        return None

    def wait_until_disappears(self,
                             search_function: Callable[[], Any],
                             timeout: Optional[int] = None,
                             check_interval: float = 0.1,
                             description: str = "elemento") -> bool:
        """
        Aguarda até que um elemento desapareça.

        Args:
            search_function (Callable): Função de busca que retorna o elemento ou None
            timeout (int, optional): Timeout em segundos. Se None, usa configuração global
            check_interval (float): Intervalo entre verificações em segundos
            description (str): Descrição do elemento para logs

        Returns:
            bool: True se elemento desapareceu, False se timeout

        Example:
            >>> def search_loading():
            ...     return bot.find_image('loading.png')
            >>>
            >>> disappeared = wait_manager.wait_until_disappears(search_loading, timeout=60)
        """
        timeout = timeout or self.config.get('wait_timeout', 30)
        start_time = time.time()
        check_count = 0

        logger.info(f"Aguardando {description} desaparecer (timeout: {timeout}s)")

        while (time.time() - start_time) < timeout:
            check_count += 1
            try:
                result = search_function()
                if not result:
                    elapsed = time.time() - start_time
                    logger.info(f"SUCESSO: {description} desapareceu após {elapsed:.1f}s (verificação #{check_count})")
                    return True
                else:
                    # Imagem ainda está visível - log apenas a cada 2 segundos para não poluir
                    elapsed = time.time() - start_time
                    if check_count == 1 or elapsed % 2.0 < check_interval or elapsed > timeout - 1:
                        logger.info(f"AGUARDANDO: {description} ainda visível após {elapsed:.1f}s (verificação #{check_count})")

            except Exception as e:
                logger.debug(f"Erro durante verificação de {description}: {e}")
                # Se há erro na busca, consideramos que desapareceu
                elapsed = time.time() - start_time
                logger.info(f"SUCESSO: {description} não encontrado (desapareceu) após {elapsed:.1f}s")
                return True

            time.sleep(check_interval)

        elapsed = time.time() - start_time
        logger.warning(f"TIMEOUT: {description} ainda visível após {elapsed:.1f}s - timeout atingido")
        return False

    def wait_with_condition(self,
                           condition_function: Callable[[], bool],
                           timeout: Optional[int] = None,
                           check_interval: float = 0.5,
                           description: str = "condição") -> bool:
        """
        Aguarda até que uma condição específica seja atendida.

        Args:
            condition_function (Callable): Função que retorna True quando condição é atendida
            timeout (int, optional): Timeout em segundos. Se None, usa configuração global
            check_interval (float): Intervalo entre verificações em segundos
            description (str): Descrição da condição para logs

        Returns:
            bool: True se condição foi atendida, False se timeout

        Example:
            >>> def check_window_active():
            ...     return bot.is_window_active('MyApp')
            >>>
            >>> success = wait_manager.wait_with_condition(check_window_active, timeout=10)
        """
        timeout = timeout or self.config.get('wait_timeout', 30)
        start_time = time.time()

        logger.debug(f"Aguardando {description} ser atendida (timeout: {timeout}s)")

        while (time.time() - start_time) < timeout:
            try:
                if condition_function():
                    elapsed = time.time() - start_time
                    logger.debug(f"{description} atendida após {elapsed:.1f}s")
                    return True

            except Exception as e:
                logger.debug(f"Erro durante verificação de {description}: {e}")

            time.sleep(check_interval)

        elapsed = time.time() - start_time
        logger.debug(f"Timeout atingido para {description} após {elapsed:.1f}s")
        return False

    def create_image_search_function(self, image_path: str, **search_kwargs) -> Callable[[], Any]:
        """
        Cria função de busca de imagem para usar com métodos de wait.

        Args:
            image_path (str): Caminho para a imagem
            **search_kwargs: Argumentos para função de busca de imagem

        Returns:
            Callable: Função que executa busca de imagem

        Example:
            >>> search_func = wait_manager.create_image_search_function(
            ...     'button.png', confidence=0.9, region=(100, 100, 200, 50)
            ... )
            >>> result = wait_manager.wait_until_found(search_func)
        """
        def search_image():
            # Esta função será definida quando integrada com TaskExecutor
            # Por agora, retorna None como placeholder
            return None

        return search_image

    def create_text_search_function(self, text: str, **search_kwargs) -> Callable[[], Any]:
        """
        Cria função de busca de texto para usar com métodos de wait.

        Args:
            text (str): Texto a buscar
            **search_kwargs: Argumentos para função de busca de texto

        Returns:
            Callable: Função que executa busca de texto

        Example:
            >>> search_func = wait_manager.create_text_search_function(
            ...     'Login', region=(50, 50, 300, 100)
            ... )
            >>> result = wait_manager.wait_until_found(search_func)
        """
        def search_text():
            # Esta função será definida quando integrada com TaskExecutor
            # Por agora, retorna None como placeholder
            return None

        return search_text

    def smart_retry(self,
                   action_function: Callable[[], Any],
                   success_condition: Callable[[Any], bool],
                   max_attempts: int = 3,
                   retry_delay: float = 1.0,
                   timeout: Optional[int] = None,
                   description: str = "operação") -> Any:
        """
        Executa uma ação com retry inteligente e condição de sucesso.

        Args:
            action_function (Callable): Função que executa a ação
            success_condition (Callable): Função que verifica se ação foi bem-sucedida
            max_attempts (int): Número máximo de tentativas
            retry_delay (float): Delay entre tentativas em segundos
            timeout (int, optional): Timeout total em segundos
            description (str): Descrição da operação para logs

        Returns:
            Any: Resultado da ação se bem-sucedida, None caso contrário

        Example:
            >>> def click_button():
            ...     return bot.click_image('button.png')
            >>>
            >>> def check_success(result):
            ...     return result is not None
            >>>
            >>> result = wait_manager.smart_retry(click_button, check_success)
        """
        timeout = timeout or self.config.get('wait_timeout', 30)
        start_time = time.time()

        logger.debug(f"Iniciando retry inteligente para {description} (max: {max_attempts} tentativas, timeout: {timeout}s)")

        for attempt in range(1, max_attempts + 1):
            # Verifica timeout
            if (time.time() - start_time) >= timeout:
                logger.debug(f"Timeout atingido durante {description}")
                break

            try:
                logger.debug(f"Tentativa {attempt}/{max_attempts} para {description}")
                result = action_function()

                if success_condition(result):
                    elapsed = time.time() - start_time
                    logger.debug(f"{description} executada com sucesso na tentativa {attempt} após {elapsed:.1f}s")
                    return result

            except Exception as e:
                logger.debug(f"Erro na tentativa {attempt} para {description}: {e}")

            # Delay entre tentativas (exceto na última)
            if attempt < max_attempts:
                time.sleep(retry_delay)

        elapsed = time.time() - start_time
        logger.debug(f"{description} falhou após {max_attempts} tentativas em {elapsed:.1f}s")
        return None