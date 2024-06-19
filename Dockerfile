# Verwende das offizielle Python-Image als Basis
FROM python:3.9

# Setze das Arbeitsverzeichnis innerhalb des Containers
WORKDIR /app

# Kopiere die Abhängigkeiten in das Arbeitsverzeichnis
COPY requirements.txt .

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Codes in das Arbeitsverzeichnis
COPY . .

# Exponiere den Port 5000
EXPOSE 5000

# Starte die Anwendung
CMD ["python", "app.py"]
