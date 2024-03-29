# Sentiment Analysis Microservice

<p align="center">
  <img src="/image.png">
</p>


## Описание

Этот микросервис предоставляет API для определения настроения сообщения. Он использует модель машинного обучения для анализа текста и возвращает результат в форме позитивного, негативного или нейтрального настроения.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/nikitairl/Tone_check.git
   ```

2. Перейдите в каталог проекта:

   ```bash
   cd Tone_check

   ```

3. Запустите docker-compose:

   ```bash
   docker-compose up
   ```

## Использование

После успешного запуска микросервис будет доступен по следующему адресу:

```
http://localhost:8080/docs
```

Вы можете отправить POST-запрос по эндпойнту `/predict_sentiment` с телом запроса в формате JSON:

```json
{
  "text": "Ваш текст для анализа настроения"
}
```

## Ответ

Микросервис вернет ответ в формате JSON:

```json
{
  "Настроение": "настроение",
  "Текст": "текст",
  "Точность": "значение"
}
```

Возможные значения для поля `Настроение`: "positive", "negative", "neutral".
