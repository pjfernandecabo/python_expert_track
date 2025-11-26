# 🧩 LECCIÓN 10 — Component System, Plugins y Registries

## 🎯 Objetivos

Al terminar esta lección sabrás:

- Diseñar un sistema de componentes modular y desacoplado.
- Crear un sistema de plugins con descubrimiento dinámico y carga segura.
- Implementar un registry robusto (registro central de componentes/handlers).
- Aplicar buenas prácticas: versión de API, estabilidad, seguridad y testing.
- Construir un mini-proyecto: un Plugin Host que descubre y carga plugins desde un directorio.

## 🧠 1. Conceptos clave y por qué importan

- Componente: unidad funcional autocontenida (clase o módulo) con una API pública bien definida.
- Plugin: componente intercambiable que extiende la aplicación sin modificar su núcleo.
- Registry: lugar central donde se registran/descubren componentes.
- Loader/Discovery: mecanismo que encuentra plugins (módulos, entry points, archivos).
- Isolation & Safety: ejecutar plugins sin que rompan el host (try/except, límites, permisos).
- Versioning / Compatibility: asegurar que plugins implementan la API esperada.

Motivos para usar plugins/registries:

- Extensibilidad sin tocar core.
- Separación de responsabilidades.
- Permitir contribuciones externas.
- Cargar/dropear funcionalidades en runtime.

## ⚙️ 2. Diseño: piezas de un sistema de plugins

- Plugin API (contract) — define lo que un plugin debe ofrecer (clases base, métodos).
- Registry — registra plugins por nombre / tipo / versión.
- Loader — descubre y carga plugins (filesystem, importlib, pkg_resources/entry_points).
- Host — usa los plugins, gestiona lifecycle (init, start, stop).
- Isolation — captura excepciones, timeouts, sandboxing si se necesita.
- Metadata — versión del plugin, author, capabilities.

Patrón recomendado: definir una clase base (`PluginBase`) o un Protocol que los plugins implementen. Registrar con un decorador o metaclase.