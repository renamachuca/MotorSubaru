# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos y el código
COPY requirements.txt requirements.txt
COPY app app

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app/__init__.py"]
