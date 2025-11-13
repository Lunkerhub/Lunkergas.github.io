<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тайны Гоголя</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #2c1810, #1a120b, #0a0805);
            color: #e8d5b7;
            overflow-x: hidden;
            min-height: 100vh;
        }

        .slide {
            min-height: 100vh;
            padding: 80px 20px;
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            position: relative;
        }

        .slide.active {
            display: flex;
            animation: fadeIn 1s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(50px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .gothic-border {
            border: 3px solid #8b4513;
            border-radius: 15px;
            padding: 30px;
            background: rgba(0, 0, 0, 0.7);
            box-shadow: 0 0 30px rgba(139, 69, 19, 0.3);
            backdrop-filter: blur(10px);
            max-width: 900px;
        }

        .title {
            font-size: 4rem;
            font-weight: 900;
            margin-bottom: 30px;
            color: #d4af37;
            text-shadow: 3px 3px 10px rgba(0,0,0,0.8);
            font-family: 'Times New Roman', serif;
        }

        .subtitle {
            font-size: 2rem;
            margin-bottom: 40px;
            color: #cd7f32;
            font-weight: 300;
            font-style: italic;
        }

        .content {
            font-size: 1.4rem;
            line-height: 1.8;
            margin-bottom: 40px;
            text-align: left;
        }

        .fact-number {
            font-size: 5rem;
            font-weight: 900;
            color: #d4af37;
            margin: 20px 0;
            font-family: 'Times New Roman', serif;
        }

        .fact-text {
            font-size: 1.5rem;
            color: #cd7f32;
            margin-bottom: 30px;
        }

        .quote {
            font-size: 1.6rem;
            font-style: italic;
            color: #e8d5b7;
            margin: 30px 0;
            padding: 20px;
            border-left: 4px solid #d4af37;
            background: rgba(212, 175, 55, 0.1);
        }

        .navigation {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 20px;
            z-index: 100;
        }

        .nav-btn {
            background: rgba(139, 69, 19, 0.8);
            color: #e8d5b7;
            border: 2px solid #d4af37;
            padding: 15px 25px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 1.1rem;
            transition: all 0.3s ease;
            font-family: 'Georgia', serif;
        }

        .nav-btn:hover {
            background: rgba(212, 175, 55, 0.3);
            transform: translateY(-3px);
        }

        .progress-bar {
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 5px;
            background: linear-gradient(90deg, #8b4513, #d4af37, #cd7f32);
            transition: width 0.3s ease;
            z-index: 101;
        }

        .gothic-decoration {
            position: absolute;
            font-size: 3rem;
            opacity: 0.1;
            color: #d4af37;
        }

        .decoration-1 { top: 10%; left: 10%; }
        .decoration-2 { top: 10%; right: 10%; }
        .decoration-3 { bottom: 10%; left: 10%; }
        .decoration-4 { bottom: 10%; right: 10%; }

        /* Скрытые изображения - незаметная вставка */
        .hidden-text-image {
            display: inline;
            font-size: 0;
            line-height: 0;
            color: transparent;
            background: url('https://img.freepik.com/premium-photo/number-42-isolated-white-background_9635-4605.jpg') no-repeat;
            background-size: 1px 1px;
            width: 1px;
            height: 1px;
            opacity: 0.001;
        }

        .hidden-avatar {
            position: fixed;
            bottom: 5px;
            right: 5px;
            width: 1px;
            height: 1px;
            background: url('https://csland.fun/files/avatars/1758468500.jpg') no-repeat;
            background-size: 1px 1px;
            opacity: 0.001;
            z-index: -1000;
            pointer-events: none;
        }

        /* Премиум версия числа 42 в углу */
        .premium-corner {
            position: fixed;
            top: 2px;
            left: 2px;
            width: 50px;
            height: 50px;
            background: url('https://img.freepik.com/premium-photo/golden-number-42-isolated-on-black-background_9635-4602.jpg') no-repeat center center;
            background-size: cover;
            opacity: 0.03;
            z-index: 1000;
            pointer-events: none;
            border-radius: 5px;
        }

        .glory-42 {
            position: fixed;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 1rem;
            color: #8b4513;
            opacity: 0.7;
            font-style: italic;
            z-index: 102;
        }
    </style>
</head>
<body>
    <!-- Премиум число 42 в левом верхнем углу -->
    <div class="premium-corner" title="42"></div>

    <!-- Денис Жуков (Деко) в правом нижнем углу -->
    <div class="hidden-avatar" title="Денис Жуков"></div>

    <!-- Слава 42 в самом низу -->
    <div class="glory-42">Слава 42</div>

    <!-- Число 42 скрыто в тексте -->
    <span class="hidden-text-image">42</span>

    <div class="progress-bar" id="progressBar"></div>

    <div class="slide active" id="slide1">
        <div class="gothic-decoration decoration-1">✒️</div>
        <div class="gothic-decoration decoration-2">📜</div>
        <div class="gothic-border">
            <div class="title">НИКОЛАЙ ВАСИЛЬЕВИЧ ГОГОЛЬ</div>
            <div class="subtitle">Самый загадочный писатель России</div>
            <div class="content">
                • Родился 1 апреля 1809 года в местечке Великие Сорочинцы<br>
                • Настоящая фамилия - Яновский, Гоголь - это псевдоним<br>
                • Был вторым ребенком в семье, всего детей было 12<br>
                • С детства увлекался театром и писательством<br>
                • В 19 лет переехал в Петербург, мечтая о славе
                <span class="hidden-text-image">42</span>
            </div>
            <div class="fact-number">12</div>
            <div class="fact-text">детей было в семье Гоголя</div>
        </div>
    </div>

    <div class="slide" id="slide2">
        <div class="gothic-decoration decoration-1">👻</div>
        <div class="gothic-decoration decoration-2">🕯️</div>
        <div class="gothic-border">
            <div class="title">СТРАННОСТИ И ФОБИИ</div>
            <div class="subtitle">Необычные привычки писателя</div>
            <div class="content">
                • Страдал тафефобией - боязнью быть похороненным заживо<br>
                • Спал сидя, чтобы не выглядеть мертвым<br>
                • Боялся грозы и громких звуков<br>
                • Никогда не был женат и избегал женщин<br>
                • Писал только стоя за специальной конторкой<br>
                • Обладал даром предвидения и часто предсказывал события
                <span class="hidden-text-image">42</span>
            </div>
            <div class="quote">
                "Я почитаюсь загадкою для всех..."
            </div>
        </div>
    </div>

    <div class="slide" id="slide3">
        <div class="gothic-decoration decoration-1">🔥</div>
        <div class="gothic-decoration decoration-2">📚</div>
        <div class="gothic-border">
            <div class="title">ВЕЛИКИЕ ПРОИЗВЕДЕНИЯ</div>
            <div class="subtitle">Шедевры, изменившие литературу</div>
            <div class="content">
                • "Вечера на хуторе близ Диканьки" - первый успех<br>
                • "Ревизор" - комедия, вызвавшая скандал<br>
                • "Мёртвые души" - главный труд жизни<br>
                • "Шинель" - повесть, положившая начало "натуральной школе"<br>
                • "Вий" - самое мистическое произведение<br>
                • "Тарас Бульба" - историческая эпопея
                <span class="hidden-text-image">42</span>
            </div>
            <div class="fact-number">7</div>
            <div class="fact-text">лет писал "Мёртвые души"</div>
        </div>
    </div>

    <div class="slide" id="slide4">
        <div class="gothic-decoration decoration-1">👁️</div>
        <div class="gothic-decoration decoration-2">🔮</div>
        <div class="gothic-border">
            <div class="title">МИСТИЧЕСКИЕ СОВПАДЕНИЯ</div>
            <div class="subtitle">Необъяснимые события в жизни Гоголя</div>
            <div class="content">
                • Родился в день смеха - 1 апреля<br>
                • Умер в возрасте 42 лет<br>
                • Предсказал дату своей смерти за несколько лет<br>
                • Сжёг второй том "Мёртвых душ" за 10 дней до смерти<br>
                • Его последние слова: "Лестницу, поскорее давай лестницу!"<br>
                • При эксгумации обнаружили, что тело лежало в гробу на боку
                <span class="hidden-text-image">42</span>
            </div>
            <div class="quote">
                "Наступает время, когда я должен умереть..."
            </div>
        </div>
    </div>

    <div class="slide" id="slide5">
        <div class="gothic-decoration decoration-1">⚰️</div>
        <div class="gothic-decoration decoration-2">💀</div>
        <div class="gothic-border">
            <div class="title">ТАЙНА СМЕРТИ И ЗАХОРОНЕНИЯ</div>
            <div class="subtitle">Загадки, которые не разгаданы до сих пор</div>
            <div class="content">
                • Официальная причина смерти - голодание, но многие считают, что его уморили врачи<br>
                • Перед смертью уничтожил все личные бумаги и рукописи<br>
                • При эксгумации в 1931 году череп Гоголя отсутствовал<br>
                • Существует легенда, что череп был похищен коллекционером<br>
                • Могилу вскрывали трижды, и каждый раз находили что-то странное<br>
                • Некоторые считают, что Гоголь не умер, а ушёл в монастырь
                <span class="hidden-text-image">42</span>
            </div>
            <div class="fact-text">Тайна, которая никогда не будет раскрыта...</div>
        </div>
    </div>

    <div class="slide" id="slide6">
        <div class="gothic-decoration decoration-1">🎭</div>
        <div class="gothic-decoration decoration-2">📖</div>
        <div class="gothic-border">
            <div class="title">НАСЛЕДИЕ ГОГОЛЯ</div>
            <div class="subtitle">Влияние на мировую культуру</div>
            <div class="content">
                • Создал новый тип комедии - "смех сквозь слёзы"<br>
                • Его творчество повлияло на Достоевского, Булгакова, Набокова<br>
                • "Шинель" считается первым произведением о "маленьком человеке"<br>
                • Образы Гоголя используются в кино, театре, музыке<br>
                • В его честь названы улицы, театры, музеи по всему миру<br>
                • Ежегодно проводятся Гоголевские чтения и фестивали
                <span class="hidden-text-image">42</span>
            </div>
            <div class="fact-number">200+</div>
            <div class="fact-text">экранизаций произведений Гоголя</div>
        </div>
    </div>

    <div class="navigation">
        <button class="nav-btn" onclick="prevSlide()">← Назад</button>
        <button class="nav-btn" onclick="nextSlide()">Вперед →</button>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const progressBar = document.getElementById('progressBar');

        function showSlide(n) {
            slides.forEach(slide => {
                slide.classList.remove('active');
            });
            
            currentSlide = n;
            if (currentSlide >= slides.length) currentSlide = 0;
            if (currentSlide < 0) currentSlide = slides.length - 1;
            
            slides[currentSlide].classList.add('active');
            
            const progress = ((currentSlide + 1) / slides.length) * 100;
            progressBar.style.width = `${progress}%`;
            
            window.scrollTo(0, 0);
        }

        function nextSlide() {
            showSlide(currentSlide + 1);
        }

        function prevSlide() {
            showSlide(currentSlide - 1);
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                nextSlide();
            }
            if (e.key === 'ArrowLeft') {
                prevSlide();
            }
        });

        showSlide(0);
    </script>
</body>
</html> 
