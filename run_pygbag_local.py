import os
import sys
import subprocess

# Пакеты для сборки
PACKAGES = [
    "pygame_static",
    "numpy"
]

# Путь к иконке
ICON_PATH = "favicon.png"  # относительный путь для pygbag

# URL CDN для pygbag
CDN_URL = "https://pygame-web.github.io/archives/0.9/"

# Имя приложения
APP_NAME = "essencepath"

# Основной скрипт проекта
MAIN_SCRIPT = os.path.join(os.getcwd(), "main.py")

if not os.path.isfile(MAIN_SCRIPT):
    print(f"❌ Не найден основной скрипт: {MAIN_SCRIPT}")
    sys.exit(1)

# Проверка установки pygbag
try:
    import pygbag
except ImportError:
    print("⚠️ pygbag не установлен. Устанавливаем...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygbag"])

# Формирование команды сборки
cmd = [
    sys.executable, "-m", "pygbag",
    "--build",
    "--app_name", APP_NAME,
    "--icon", ICON_PATH,
    "--cdn", CDN_URL
]

# Добавляем пакеты
for pkg in PACKAGES:
    cmd += ["--package", pkg]

# Основной скрипт в конце
cmd.append(MAIN_SCRIPT)

print("🚧 Запуск сборки с pygbag...")
print("Команда:", " ".join(cmd))

try:
    subprocess.check_call(cmd)
    print("✅ Сборка завершена успешно!")
except subprocess.CalledProcessError as e:
    print(f"❌ Ошибка при сборке pygbag: {e}")
