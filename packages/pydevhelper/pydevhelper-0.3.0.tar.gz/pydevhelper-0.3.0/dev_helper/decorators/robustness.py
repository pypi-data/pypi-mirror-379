import time
import logging
import functools
from typing import Callable, Any, TypeVar, Tuple

F = TypeVar("F", bound=Callable[..., Any])

def retry(
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[type[BaseException], ...] = (Exception,),
    sleep_func: Callable[[float], None] = time.sleep,
    log_success: bool = False,
    logger: logging.Logger = logging.getLogger()
) -> Callable[[F], F]:
    """
    Um decorator que tenta executar uma função novamente em caso de exceções configuráveis.

    Args:
        tries (int, optional): Número máximo de tentativas. Padrão é 3.
        delay (float, optional): Atraso inicial em segundos entre tentativas. Padrão é 1.
        backoff (float, optional): Multiplicador para aumentar o atraso a cada tentativa. Padrão é 2.
        exceptions (tuple, optional): Exceções que disparam retry. Default = (Exception,).
        sleep_func (callable, optional): Função de espera (padrão = time.sleep). 
                                         Pode ser substituída em testes para evitar atrasos.
        log_success (bool, optional): Se True, loga sucesso após retries.
        logger (logging.Logger, optional): Instância do logger.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_tries, current_delay = tries, delay

            while current_tries > 0:
                try:
                    result = func(*args, **kwargs)
                    if log_success and current_tries < tries:
                        logger.info(
                            f"Função '{func.__name__}' executada com sucesso após retries."
                        )
                    return result
                except exceptions as e:
                    current_tries -= 1

                    if current_tries == 0:
                        logger.error(
                            f"Função '{func.__name__}' falhou após {tries} tentativas. "
                            f"Último erro: {e}"
                        )
                        raise

                    logger.warning(
                        f"Função '{func.__name__}' falhou com o erro: {e}. "
                        f"A tentar novamente em {current_delay:.2f}s... "
                        f"({current_tries} tentativas restantes)"
                    )
                    sleep_func(current_delay)
                    current_delay *= backoff

        return wrapper  # type: ignore
    return decorator
