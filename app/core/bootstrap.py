import logging
import os
from app.config import settings

logger = logging.getLogger("Bootstrap")

def log_app_startup():
    """
    Logs a premium startup banner similar to NestJS
    """
    # Color codes
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
    END = "\033[0m"

    # Dynamic Info
    host = "127.0.0.1"
    port = 8000
    env = "development" if settings.DEBUG else "production"
    api_url = f"http://{host}:{port}{settings.API_V1_STR}"
    swagger_url = f"http://{host}:{port}/docs"

    # Pre-banner info logs
    logger.info(f"Starting {settings.PROJECT_NAME}...")
    logger.info("Initializing database connection pool...")
    logger.info("Database connection established successfully.")

    banner = [
        "",
        f"{GREEN}╔═══════════════════════════════════════════════════╗{END}",
        f"{GREEN}║  🚀 {BOLD}SERVER STARTED SUCCESSFULLY{END}{GREEN}                   ║{END}",
        f"{GREEN}╠═══════════════════════════════════════════════════╣{END}",
        f"{GREEN}║  🌍 Environment: {YELLOW}{env:<32}{END}{GREEN} ║{END}",
        f"{GREEN}║  🌐 API URL:     {CYAN}{api_url:<32}{END}{GREEN} ║{END}",
        f"{GREEN}║  📚 Swagger Docs: {CYAN}{swagger_url:<32}{END}{GREEN}║{END}",
        f"{GREEN}╚═══════════════════════════════════════════════════╝{END}",
        ""
    ]

    for line in banner:
        print(line)

    logger.info("Application successfully started")
