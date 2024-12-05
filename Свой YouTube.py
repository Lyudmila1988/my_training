import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password):
        """Хэширует пароль"""
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __repr__(self):
        return f"User(nickname='{self.nickname}', age={self.age})"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video(title='{self.title}', duration={self.duration}s, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """Авторизация пользователя"""
        hashed_password = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Добро пожаловать, {nickname}!")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        """Регистрация нового пользователя"""
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Пользователь {nickname} успешно зарегистрирован и вошел в систему!")

    def log_out(self):
        """Выход из текущего аккаунта"""
        if self.current_user:
            print(f"До свидания, {self.current_user.nickname}!")
        self.current_user = None

    def add(self, *videos):
        """Добавление видео"""
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, keyword):
        """Поиск видео по ключевому слову"""
        keyword_lower = keyword.lower()
        return [video.title for video in self.videos if keyword_lower in video.title.lower()]

    def watch_video(self, title):
        """Просмотр видео"""
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Начинаем просмотр: {title}")
        for second in range(video.time_now + 1, video.duration + 1):
            print(second, end=" ", flush=True)
            time.sleep(0.1)  # Эмулируем задержку в одну секунду
        print("\nКонец видео")
        video.time_now = 0  # Сброс времени просмотра

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')

