
# Gestión de Clientes para Axanet

Este repositorio contiene una aplicación en Python desarrollada para la empresa Axanet. La aplicación permite gestionar los datos de clientes en archivos JSON, posibilitando el registro de nuevos clientes, la actualización de información de clientes recurrentes, y la consulta o eliminación de registros. Este proyecto también incluye flujos de trabajo automatizados en GitHub Actions para notificar al equipo sobre la creación, actualización y consulta de clientes.

## Contenidos
- [Objetivos](#objetivos)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Flujos de GitHub Actions](#flujos-de-github-actions)

## Objetivos
1. **Registrar nuevos clientes** y almacenar su información en archivos JSON.
2. **Actualizar información** de clientes recurrentes añadiendo nuevos servicios solicitados.
3. **Consultar y eliminar** información de clientes existentes.
4. **Automatizar flujos de trabajo** para generar notificaciones al equipo en caso de creación, actualización o consulta de clientes.

## Requisitos
- Python 3.x
- Git
- Cuenta de GitHub (para colaborar y probar los flujos de GitHub Actions)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/axanet-gestion-clientes.git
   ```
2. Entra en el directorio del proyecto:
   ```bash
   cd axanet-gestion-clientes
   ```
3. Instala las dependencias necesarias (si las hay).

## Uso

### Ejecutar el programa principal
El archivo principal, `gestor_clientes.py`, contiene las funciones para gestionar la información de los clientes. Para iniciar el programa, ejecuta:

```bash
python gestor_clientes.py
```

### Funciones principales
- **Agregar cliente**: Registra un nuevo cliente y crea su archivo de datos.
- **Actualizar cliente**: Agrega una nueva solicitud al archivo de un cliente recurrente.
- **Consultar cliente**: Muestra los datos de un cliente específico.
- **Eliminar cliente**: Elimina el archivo de un cliente.

Ejemplo:
```python
agregar_cliente("Juan Perez", "Mantenimiento anual")
consultar_cliente("Juan Perez")
actualizar_cliente("Juan Perez", "Reparación urgente")
consultar_cliente("Juan Perez")
borrar_cliente("Juan Perez")
```

## Estructura del Proyecto

```
axanet-gestion-clientes/
│
├── gestor_clientes.py        # Código fuente de la aplicación
├── .github/
│   └── workflows/            # Flujos de GitHub Actions para automatización
│       ├── nuevo_cliente.yml # Notificación para la creación de nuevos clientes
│       ├── actualizar_cliente.yml # Notificación para la actualización de clientes recurrentes
│       └── consulta_cliente.yml # Notificación para la consulta de clientes
└── README.md                 # Este archivo README
```

## Flujos de GitHub Actions

Para mejorar la colaboración en el proyecto, se han configurado tres flujos en GitHub Actions:

1. **Nuevo Cliente** (`nuevo_cliente.yml`): Este flujo se activa al añadir un nuevo cliente. Notifica al equipo con un mensaje: “Nuevo cliente creado. Notificación enviada al equipo.”
   
2. **Actualización Cliente** (`actualizar_cliente.yml`): Este flujo se ejecuta al actualizar un cliente recurrente, notificando con el mensaje: “Cliente recurrente actualizado. Notificación enviada al equipo.”

3. **Consulta Cliente** (`consulta_cliente.yml`): Este flujo notifica al equipo cuando se realiza una consulta, con el mensaje: “Consulta realizada en el sistema. Notificación enviada al equipo.”

Estos flujos están ubicados en la carpeta `.github/workflows` y se activan automáticamente según los cambios en el archivo `gestor_clientes.py`.

## Contribución

1. Haz un fork de este repositorio y clónalo en tu máquina local.
2. Crea una nueva rama para tu contribución:
   ```bash
   git checkout -b nombre-rama
   ```
3. Realiza los cambios y sube los commits a tu rama.
4. Abre un pull request en este repositorio con la descripción de tus cambios.

## Licencia
Este proyecto es de uso exclusivo para el desarrollo de soluciones de gestión de clientes para la empresa Axanet.

## Enlaces
- **Repositorio GitHub**: [https://github.com/usuario/axanet-gestion-clientes](https://github.com/usuario/axanet-gestion-clientes)
