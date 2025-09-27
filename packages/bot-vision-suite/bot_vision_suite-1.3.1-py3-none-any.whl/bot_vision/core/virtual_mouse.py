"""

Bot Vision Suite - Virtual Mouse



Este módulo implementa funcionalidade de mouse virtual que permite

realizar cliques sem mover o cursor físico do mouse.

"""



import time
import logging
import platform
import ctypes
from typing import Tuple, Optional

from ..utils.config import BotVisionConfig



logger = logging.getLogger(__name__)





class VirtualMouse:

    """

    Classe para controle de mouse virtual que permite cliques

    sem mover o cursor físico do mouse.

    """



    def __init__(self, config: Optional[BotVisionConfig] = None):

        """

        Inicializa o mouse virtual.



        Args:

            config (BotVisionConfig, optional): Configuração da biblioteca

        """

        from ..utils.config import get_default_config

        self.config = config or get_default_config()

        self.system = platform.system().lower()

        self.original_cursor_pos = None



        # Detecta se mouse virtual está disponível no sistema

        self.virtual_available = self._check_virtual_mouse_availability()



        if not self.virtual_available and self.config.get('use_virtual_mouse', False):

            logger.warning("ATENCAO: use_virtual_mouse=True mas mouse virtual nao disponivel no sistema!")

            logger.warning("FALLBACK: Todos os cliques usarao mouse fisico")



    def _check_virtual_mouse_availability(self) -> bool:

        """

        Verifica se mouse virtual está disponível no sistema atual.



        Returns:

            bool: True se mouse virtual está disponível

        """

        if self.system == "windows":

            try:

                import win32gui

                import win32con

                import win32api

                return True

            except ImportError:

                logger.debug("Módulos win32 não disponíveis. Mouse virtual Windows indisponível.")

                return False

        elif self.system in ["linux", "darwin"]:

            # Para Linux/macOS, pode implementar usando Xlib ou outras bibliotecas

            # Por agora, retorna False para usar fallback

            logger.debug(f"Mouse virtual não implementado para {self.system}. Usando fallback.")

            return False



        return False



    def _get_windows_dpi_scale(self, hwnd: int) -> Tuple[float, float]:
        if self.system != "windows" or not hwnd:
            return 1.0, 1.0

        scale_x = scale_y = 1.0
        try:
            user32 = ctypes.windll.user32
            get_dpi_for_window = getattr(user32, "GetDpiForWindow", None)
            if get_dpi_for_window:
                dpi = get_dpi_for_window(hwnd)
                if dpi:
                    scale = dpi / 96.0
                    return scale, scale

            monitor = None
            monitor_from_window = getattr(user32, "MonitorFromWindow", None)
            if monitor_from_window:
                MONITOR_DEFAULTTONEAREST = 2
                monitor = monitor_from_window(hwnd, MONITOR_DEFAULTTONEAREST)

            if monitor:
                try:
                    shcore = ctypes.windll.shcore
                except AttributeError:
                    shcore = None

                if shcore:
                    MDT_EFFECTIVE_DPI = 0
                    dpi_x = ctypes.c_uint()
                    dpi_y = ctypes.c_uint()
                    result = shcore.GetDpiForMonitor(
                        monitor,
                        MDT_EFFECTIVE_DPI,
                        ctypes.byref(dpi_x),
                        ctypes.byref(dpi_y)
                    )
                    if result == 0:
                        if dpi_x.value:
                            scale_x = dpi_x.value / 96.0
                        if dpi_y.value:
                            scale_y = dpi_y.value / 96.0
        except Exception as e:
            logger.debug(f"Falha ao obter escala DPI: {e}")
        return scale_x, scale_y

    def _resolve_client_coordinates(
        self,
        hwnd: int,
        logical_point: Tuple[int, int],
        scale_x: float,
        scale_y: float,
    ) -> Tuple[int, int, int, int]:
        import win32gui

        scale_x = scale_x or 1.0
        scale_y = scale_y or 1.0

        screen_x = int(round(logical_point[0] * scale_x))
        screen_y = int(round(logical_point[1] * scale_y))

        try:
            origin = win32gui.ClientToScreen(hwnd, (0, 0))
            origin_x = int(round(origin[0] * scale_x))
            origin_y = int(round(origin[1] * scale_y))
            return screen_x - origin_x, screen_y - origin_y, screen_x, screen_y
        except Exception as ex:
            logger.debug(f"Fallback ScreenToClient apos erro ClientToScreen: {ex}")
            try:
                client_x, client_y = win32gui.ScreenToClient(hwnd, logical_point)
                client_x = int(round(client_x * scale_x))
                client_y = int(round(client_y * scale_y))
                return client_x, client_y, screen_x, screen_y
            except Exception as inner:
                logger.debug(f"Falha ao converter coordenadas para cliente: {inner}")
                return screen_x, screen_y, screen_x, screen_y

    def save_cursor_position(self):

        """Salva a posição atual do cursor."""

        try:

            import pyautogui

            self.original_cursor_pos = pyautogui.position()

            logger.debug(f"Posição do cursor salva: {self.original_cursor_pos}")

        except Exception as e:

            logger.debug(f"Erro ao salvar posição do cursor: {e}")



    def restore_cursor_position(self):

        """Restaura o cursor para posição original."""

        if self.original_cursor_pos:

            try:

                import pyautogui

                pyautogui.moveTo(self.original_cursor_pos.x, self.original_cursor_pos.y, duration=0)

                logger.debug(f"Cursor restaurado para: {self.original_cursor_pos}")

            except Exception as e:

                logger.debug(f"Erro ao restaurar posição do cursor: {e}")





    def _click_virtual_windows(self, x: int, y: int, button: str = 'left') -> bool:
        """
        Executa clique virtual no Windows usando Win32 API.

        Args:
            x (int): Coordenada X
            y (int): Coordenada Y
            button (str): Botão do mouse ('left', 'right', 'double')

        Returns:
            bool: True se clique foi executado com sucesso
        """
        try:
            import win32gui
            import win32con
            import win32api

            logical_point = (int(round(x)), int(round(y)))

            hwnd = win32gui.WindowFromPoint(logical_point)
            if not hwnd:
                return False

            scale_x, scale_y = self._get_windows_dpi_scale(hwnd)
            scale_x = scale_x or 1.0
            scale_y = scale_y or 1.0

            client_x, client_y, screen_x, screen_y = self._resolve_client_coordinates(
                hwnd,
                logical_point,
                scale_x,
                scale_y,
            )

            if client_x < 0 or client_y < 0:
                logger.debug(f"Coordenadas fora da area cliente: ({client_x}, {client_y})")
                return False

            if scale_x != 1.0 or scale_y != 1.0:
                logger.debug(
                    f"Aplicando escala DPI ({scale_x:.3f}, {scale_y:.3f}) para tela ({screen_x}, {screen_y})"
                )

            lParam = win32api.MAKELONG(int(client_x), int(client_y))

            # Garante que a janela receba a posicao atualizada antes do clique
            win32gui.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)

            if button == 'left':
                win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
                time.sleep(0.05)
                win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
            elif button == 'right':
                win32gui.PostMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
                time.sleep(0.05)
                win32gui.PostMessage(hwnd, win32con.WM_RBUTTONUP, 0, lParam)
            elif button == 'double':
                win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
                time.sleep(0.05)
                win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
                time.sleep(0.05)
                win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
                time.sleep(0.05)
                win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

            window_title = win32gui.GetWindowText(hwnd)
            logger.debug(
                f"Clique virtual executado em janela: {window_title} - tela ({screen_x}, {screen_y}) -> cliente ({client_x}, {client_y})"
            )
            return True

        except Exception as e:
            logger.debug(f"Erro no clique virtual Windows: {e}")
            return False

    def _click_virtual_linux(self, x: int, y: int, button: str = 'left') -> bool:

        """

        Executa clique virtual no Linux (placeholder para implementação futura).



        Args:

            x (int): Coordenada X

            y (int): Coordenada Y

            button (str): Botão do mouse



        Returns:

            bool: True se clique foi executado com sucesso

        """

        # TODO: Implementar usando Xlib ou outras bibliotecas Linux

        logger.debug("Clique virtual Linux não implementado. Usando fallback.")

        return False



    def _click_virtual_macos(self, x: int, y: int, button: str = 'left') -> bool:

        """

        Executa clique virtual no macOS (placeholder para implementação futura).



        Args:

            x (int): Coordenada X

            y (int): Coordenada Y

            button (str): Botão do mouse



        Returns:

            bool: True se clique foi executado com sucesso

        """

        # TODO: Implementar usando Quartz ou outras bibliotecas macOS

        logger.debug("Clique virtual macOS não implementado. Usando fallback.")

        return False



    def click(self, x: int, y: int, button: str = 'left', use_virtual: Optional[bool] = None, location_info: Optional[tuple] = None) -> bool:

        """

        Executa clique usando mouse virtual ou físico baseado na configuração.



        Args:

            x (int): Coordenada X

            y (int): Coordenada Y

            button (str): Botão do mouse ('left', 'right', 'double', 'move_to')

            use_virtual (bool, optional): Forçar uso de mouse virtual (sobrescreve configuração)

            location_info (tuple, optional): Informação da região encontrada (x, y, width, height) para recalcular centro



        Returns:

            bool: True se clique foi executado com sucesso

        """

        # Determina se deve usar mouse virtual

        should_use_virtual = use_virtual if use_virtual is not None else self.config.get('use_virtual_mouse', False)



        # Se está usando virtual mouse e tem informação da localização, recalcula centro exato

        if should_use_virtual and location_info:

            center_x = location_info[0] + (location_info[2] // 2)

            center_y = location_info[1] + (location_info[3] // 2)

            logger.info(f"VIRTUAL: Recalculando centro da imagem: original({x}, {y}) -> centro_exato({center_x}, {center_y})")

            x, y = center_x, center_y



        # Se é apenas movimento, não precisa de clique virtual

        if button == 'move_to':

            return self._move_to_physical(x, y)



        # Tenta mouse virtual se disponível e configurado

        if should_use_virtual and self.virtual_available:

            logger.info(f"Executando clique VIRTUAL em ({x}, {y}) com botão {button}")



            if self.system == "windows":

                success = self._click_virtual_windows(x, y, button)

                if success:

                    logger.info(f"SUCESSO: Clique virtual executado com sucesso em ({x}, {y})")

                    return True

                else:

                    logger.warning(f"FALHA: Clique virtual falhou em ({x}, {y}) - fazendo fallback para mouse fisico")

            elif self.system == "linux":

                success = self._click_virtual_linux(x, y, button)

                if success:

                    logger.info(f"SUCESSO: Clique virtual Linux executado com sucesso em ({x}, {y})")

                    return True

                else:

                    logger.warning(f"FALHA: Clique virtual Linux falhou em ({x}, {y}) - fazendo fallback para mouse fisico")

            elif self.system == "darwin":

                success = self._click_virtual_macos(x, y, button)

                if success:

                    logger.info(f"SUCESSO: Clique virtual macOS executado com sucesso em ({x}, {y})")

                    return True

                else:

                    logger.warning(f"FALHA: Clique virtual macOS falhou em ({x}, {y}) - fazendo fallback para mouse fisico")



        # Fallback para mouse físico

        if should_use_virtual:

            logger.warning(f"FALLBACK: use_virtual_mouse=True mas usando mouse fisico em ({x}, {y})")

        else:

            logger.info(f"Executando clique FISICO em ({x}, {y}) com botao {button}")



        return self._click_physical(x, y, button)



    def _move_to_physical(self, x: int, y: int) -> bool:

        """

        Move o cursor para posição especificada.



        Args:

            x (int): Coordenada X

            y (int): Coordenada Y



        Returns:

            bool: True se movimento foi executado com sucesso

        """

        try:

            import pyautogui

            pyautogui.moveTo(x, y, duration=self.config.get('movement_duration', 0.1))

            logger.debug(f"Cursor movido para ({x}, {y})")

            return True

        except Exception as e:

            logger.error(f"Erro ao mover cursor: {e}")

            return False



    def _click_physical(self, x: int, y: int, button: str) -> bool:

        """

        Executa clique usando mouse físico com preservação de posição.



        Args:

            x (int): Coordenada X

            y (int): Coordenada Y

            button (str): Botão do mouse



        Returns:

            bool: True se clique foi executado com sucesso

        """

        try:

            import pyautogui



            # Salva posição atual se mouse virtual estava tentado ser usado

            should_preserve = self.config.get('use_virtual_mouse', False)

            if should_preserve:

                self.save_cursor_position()



            # Executa clique físico

            if button == 'left':

                pyautogui.click(x, y, duration=self.config.get('click_duration', 0.1))

            elif button == 'right':

                pyautogui.rightClick(x, y)

            elif button == 'double':

                pyautogui.doubleClick(x, y)

            elif button == 'move_to':

                pyautogui.moveTo(x, y, duration=self.config.get('movement_duration', 0.1))



            # Restaura posição se estava usando mouse virtual

            if should_preserve:

                self.restore_cursor_position()



            logger.debug(f"Clique físico executado em ({x}, {y}) com botão {button}")

            return True



        except Exception as e:

            logger.error(f"Erro no clique físico: {e}")

            return False



    def is_virtual_available(self) -> bool:

        """

        Verifica se mouse virtual está disponível.



        Returns:

            bool: True se mouse virtual está disponível

        """

        return self.virtual_available



    def get_cursor_position(self) -> Optional[Tuple[int, int]]:

        """

        Obtém posição atual do cursor.



        Returns:

            Tuple[int, int]: Coordenadas (x, y) do cursor ou None se erro

        """

        try:

            import pyautogui

            pos = pyautogui.position()

            return (pos.x, pos.y)

        except Exception as e:

            logger.error(f"Erro ao obter posição do cursor: {e}")

            return None