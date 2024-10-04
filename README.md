# Subaru's Motor
Subaru's Motor
Subaru's Motor es un proyecto que utiliza una arquitectura de microservicios para gestionar productos y pedidos.
Estructura del Proyecto



MotorSubaru/
│
├── orders/                         
│   ├── app/
│   │   ├── __init__.py            
│   │   ├── models.py                
│   │   ├── routes.py                
│   │   ├── config.py               
│   │   └── wsgi.py                 
│   └── tests/                     
│
├── products/                      
│   ├── app/
│   │   ├── __init__.py             
│   │   ├── models.py                
│   │   ├── routes.py               
│   │   ├── config.py            
│   │   └── wsgi.py                 
│   └── tests/                      
│
├── config/                         
│   ├── database.py                 
│   └── settings.py              
│
├── docs/                            
│
├── venv/                           
│
├── requirements.txt               
│
├── README.md                      
│
└── .gitignore                      




Descripción de los Componentes
Servicio de Productos

Ubicación: /products/
Descripción: Este servicio maneja toda la lógica relacionada con los productos.
Archivos principales:

models.py: Define los modelos de datos para los productos.
routes.py: Contiene las rutas y la lógica de la API para los productos.



Servicio de Pedidos

Ubicación: /orders/
Descripción: Este servicio maneja toda la lógica relacionada con los pedidos.
Archivos principales:

models.py: Define los modelos de datos para los pedidos.
routes.py: Contiene las rutas y la lógica de la API para los pedidos.



Configuración y Ejecución
Este proyecto utiliza Docker para facilitar la configuración y ejecución de los servicios.

Asegúrate de tener Docker y Docker Compose instalados en tu sistema.
Clona este repositorio:
Copygit clone https://github.com/tu-usuario/subaru-motor.git
cd subaru-motor

Inicia los servicios utilizando Docker Compose:
Copydocker-compose up


Esto iniciará tanto el servicio de productos como el de pedidos.
Desarrollo
Para desarrollar en este proyecto:

Cada servicio tiene su propio requirements.txt. Asegúrate de instalar las dependencias necesarias si trabajas en un entorno local.
Los Dockerfiles en cada servicio definen el entorno de ejecución. Modifícalos según sea necesario para tu entorno de desarrollo.
El archivo docker-compose.yml en la raíz del proyecto define cómo se relacionan y ejecutan los servicios. Ajústalo si añades nuevos servicios o cambias la configuración existente.

Contribuir
Si deseas contribuir a este proyecto, por favor:

Haz un fork del repositorio
Crea una nueva rama para tu característica (git checkout -b feature/AmazingFeature)
Haz commit de tus cambios (git commit -m 'Add some AmazingFeature')
Push a la rama (git push origin feature/AmazingFeature)
Abre un Pull Request

