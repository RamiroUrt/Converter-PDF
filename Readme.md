# 📄 Word to PDF Batch Converter

![Banner del proyecto](banner.png)

Un conversor de documentos **Word (.docx) a PDF** desarrollado en **Python**, capaz de convertir **múltiples archivos automáticamente** desde una carpeta de origen hacia una carpeta de destino.

---

## 🚀 Características

- ✅ Conversión por lote de archivos `.docx`
- 📁 Procesa todos los documentos de una carpeta
- 📄 Genera PDFs con el mismo nombre del archivo original
- 🛠 Manejo básico de errores
- 💻 Interacción simple por consola

---

## 🧰 Tecnologías utilizadas

- **Python 3**
- **docx2pdf**
- **os (standard library)**

---

## 📦 Requisitos

Antes de ejecutar el proyecto, asegurate de tener instalado:

- Python 3.8 o superior  
- Microsoft Word (requerido por `docx2pdf` en Windows)

Instalá la dependencia necesaria:

```bash
pip install docx2pdf
```

## ▶️ Uso

- Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/word-to-pdf-batch-converter.git

cd word-to-pdf-batch-converter
```

- Ejecutá el script:
```bash
python main.py
```

- Ingresá:

- Ruta de la carpeta que contiene los archivos .docx
⚠️Ejemplo
```bash
C:\Users\Ramiro\Desktop\WordToPdf\input_docs
```
- Ruta de la carpeta donde se guardarán los PDFs
⚠️Ejemplo
```bash
C:\Users\Ramiro\Desktop\WordToPdf\input_docs\Output_docs
```
📌 Todos los archivos .docx encontrados serán convertidos automáticamente.

📁 Ejemplo de estructura
```bash
input_docs/
 ├── contrato.docx
 ├── cv.docx
 └── informe.docx

Output_docs/
 ├── contrato.pdf
 ├── cv.pdf
 └── informe.pdf
```
## ⚠️ Notas importantes

El script solo procesa archivos con extensión .docx

La carpeta de salida se crea automáticamente si no existe

En Windows, docx2pdf requiere que Microsoft Word esté instalado
