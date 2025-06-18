# comenzando_python
Curso introductorio de python 

## Calendar summarizer

El script `calendar_summarizer.py` permite cargar un archivo de calendario en formato ICS y generar un resumen de las reuniones y recordatorios de los próximos días utilizando la API de OpenAI.

### Uso

```bash
pip install ics openai
python calendar_summarizer.py path/al-archivo.ics --days 7
```

Se requiere definir la variable de entorno `OPENAI_API_KEY` para autenticar las peticiones a OpenAI.
