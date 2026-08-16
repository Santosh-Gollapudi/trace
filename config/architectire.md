# TRACE Architecture

## Core

TraceCore is the central controller.

All modules communicate through the Core.

Modules never communicate directly.

This allows:

- Easy testing
- Plugin support
- Multiple AI providers
- Cloud/local switching
- Better maintainability