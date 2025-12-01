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

## 🧩 Buenas prácticas y consideraciones (importantes)

API & Stability

- Define claramente la interfaz (Protocol/ABC) que los plugins deben cumplir.
- Usa semantic versioning y compara versiones adecuadamente (no lexicográfico en prod).
- Mantén break changes sólo en major version bumps.

Seguridad

- Nunca ejecutes código plugin sin validación en entornos inseguros.
- Considera sandboxing (subprocess, containers) para ejecutar código desconocido.
- Limita permisos de I/O si el plugin puede acceder a FS o red.

Robustez

- try/except alrededor de setup/run.
- Timeouts en ejecución (subprocess, threads) para bloquear plugins que cuelgan.
- Validaciones de inputs/outputs (schema).

Discoverability

- Para proyectos instalables, usa entry_points (setuptools) para discovery.
- Alternativas: plugin folder, HTTP registry, database registry.

Testing

- Testea plugins con fixtures que aíslen filesystem / network.
- Proporciona un compatibility test suite que los desarrolladores de plugin pueden ejecutar para validar su plugin antes de publicar.

Lifecycle

- Define hooks: setup, start, stop, teardown.
- Admite reloading: reload_plugin (cuidado con estados).

## 🔧 Extensiones avanzadas (ideas para seguir)

- Hot-reload: detecta cambios en archivos y recarga módulos.
- Sandbox: run plugin in subprocess and communicate via IPC.
- Dependency injection: pasar servicios (DB, config, logger) al plugin en setup.
- Plugin manifests: metadata en plugin.json para validación previa.
- Entry points: discovery via pkg_resources / importlib.metadata.entry_points().

## 🧾 7. Resumen de la lección

Qué aprendiste	-> Por qué importa

- Definir Plugin API (Protocol) -> 	Establece contrato claro para extensibilidad
- Implementar Registry	-> Descubrir y versionar plugins fácilmente
- Crear Loader dinámico	-> Hacer el sistema modular y extensible en runtime
- Diseñar Host robusto	-> Ejecutar plugins de forma segura y controlada
- Buenas prácticas ->	Mantener estabilidad, seguridad y testing