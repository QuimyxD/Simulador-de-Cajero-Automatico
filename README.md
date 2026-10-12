# Simulador de Cajero Automático (Robux Bank)

Aplicación de escritorio interactiva desarrollada en **Python** con **Tkinter** que simula las operaciones principales de un cajero automático para el "Banco de Robux". El sistema permite la autenticación de usuarios, consulta de saldos en múltiples cuentas, depósitos, retiros con montos predefinidos y personalizados, transferencias entre usuarios y un historial detallado de transacciones.

---

## Objetivo

Proporcionar una interfaz gráfica intuitiva y funcional para simular las transacciones financieras habituales de un cajero automático, integrando validación de credenciales, gestión de estados y manejo de saldos para distintas cuentas (Ahorro, Corriente, Crédito).

---

## Requisitos del Sistema

- **Python** (versión 3.x recomendada)
- **Tkinter** / **ttk** (incluidos por defecto en la instalación estándar de Python)

---

## Estructura del Repositorio

```text
Simulador_Cajero/
├── Simulador cajero automatico.py   # Script principal de la aplicación
└── README.md                        # Documentación del proyecto
```

---

## Credenciales de Acceso

Para ingresar y operar en la interfaz del cajero automático, utiliza las siguientes credenciales predeterminadas:

- **Usuario:** `quim`
- **Contraseña:** `1234`

---

## Instrucciones de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/simulador-cajero-robux.git
   cd simulador-cajero-robux
   ```

2. **Ejecutar el script principal:**
   ```bash
   python "Simulador cajero automatico.py"
   ```

---

## Funcionalidades Principal

- **Autenticación:** Pantalla de bienvenida e inicio de sesión con validación de seguridad.
- **Consulta de Saldos:** Visualización del saldo actual y desglose por cuentas (Ahorro, Corriente y Crédito).
- **Depósitos:** Incremento del saldo principal con validación de montos positivos.
- **Retiros:** Selección de cuenta de origen y montos predefinidos ($5, $10, $20, $50, $100, $200, $500) o monto personalizado.
- **Transferencias:** Envío de fondos a otros usuarios registrados.
- **Historial:** Registro continuo de todas las operaciones realizadas durante la sesión.

---

## Autor y Créditos

**Cecil Quimey Azuara Yáñez**

- **Institución:** Escuela de Nivel Medio Superior Centro Histórico León (ENMSCHL UG).
- **Asignatura:** Lenguajes de Programación.
