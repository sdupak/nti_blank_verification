# Алгоритм автоматической проверки правильности загруженного документа

## Преимущества решения
- Высокая точность распознавания<br>
*При тестировании на 100 различных файлов только 3 данный алгоритм ошибочно определил как неверно загруженные и выдал рекомендации для исправления (см. Возможные ошибки).*<br>
- Высокая скорость выполнения<br>
*На процессоре Intel core i7 средняя скорость распознавания документа составила 0.92с.*<br>
- Низкие требования к ресурсам<br>
*Не требует больших вычислительных мощностей, GPU или TPU. Требует всего лишь 180MB оперативной памяти и 1.5MB на диске.*<br>
- Простое добавление новых документов<br>
*Данный алгоритм в отличии от нейронной сети не требует дата сета, он требует только один документ для того, чтобы "научится" его распознавать.*

## Подробнее: что проверяет алгоритм
- Загружен документ, а не что-либо другое
- Загружен именно тот документ который требовалось
- Текст документа полностью в кадре и читаем
- Бланк заполнен и подписан

## Возможные ошибки
*При выявлении типичных ошибок программа выдает инструкции к их исправлению.*<br>
- Неверный документ
- Документ не заполнен
- Нет подписи
- Часть документа не в кадре
- Документ не читаем
- Плохое освещение
- В кадре много лишнего (Документ находится на большом расстоянии от камеры)<br>
- При выявлении других ошибок пожалуйста сообщите разработчикам.

## Инструкция к запуску
Этот раздел требует доработки.

## Навигация по репозиторию
Основное:
- src - все исходники кода
  - work_v2.5.py
  - BlankType.py
  - BlankStatus.py
- reference - эталоны бланков
- data - примеры фотографий и сканов для тестирования алгоритма


