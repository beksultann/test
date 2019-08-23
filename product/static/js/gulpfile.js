var gulp = require('gulp'), // Подключаем Gulp
    sass = require('gulp-sass'), //Подключаем sass пакет,
    browserSync = require('browser-sync'), // Подключаем Browser Sync
    concat = require('gulp-concat'), // Подключаем gulp-concat (для конкатенации файлов)
    uglify = require('gulp-uglifyjs'), // Подключаем gulp-uglifyjs (для сжатия JS)
    cssnano = require('gulp-cssnano'), // Подключаем пакет для минификации CSS
    rename = require('gulp-rename'), // Подключаем библиотеку для переименования файлов
    del = require('del'), // Подключаем библиотеку для удаления файлов и папок
    imagemin = require('gulp-imagemin'), // Подключаем библиотеку для работы с изображениями
    pngquant = require('imagemin-pngquant'), // Подключаем библиотеку для работы с png
    autoprefixer = require('gulp-autoprefixer');// Подключаем библиотеку для автоматического добавления префиксов

gulp.task('sass', function () { // Создаем таск sass
    return gulp.src('app/sass/**/*.scss') // Берем источник
        .pipe(sass()) // Преобразуем sass в CSS посредством gulp-sass
        .pipe(autoprefixer(['last 15 versions', '> 1%', 'ie 8', 'ie 7'], {cascade: true})) // Создаем префиксы
        .pipe(concat('main.css'))
        .pipe(gulp.dest('app')) // Выгружаем результата в папку app/css
        .pipe(browserSync.reload({stream: true})) // Обновляем CSS на странице при изменении
});

gulp.task('browser-sync', function () { // Создаем таск browser-sync
    browserSync({ // Выполняем browserSync
        server: { // Определяем параметры сервера
            baseDir: 'app' // Директория для сервера - app
        },
        notify: false // Отключаем уведомления
    });
});

gulp.task('scripts', function () {
    return gulp.src([ // Берем все необходимые библиотеки
        'app/libs/jquery/dist/jquery.min.js', // Берем jQuery
        'app/libs/jquery-nice-select-1.1.0/js/jquery.nice-select.min.js',
        'app/libs/air-datepicker/dist/js/datepicker.min.js'
    ])
        .pipe(concat('libs.min.js')) // Собираем их в кучу в новом файле libs.min.js
        .pipe(uglify()) // Сжимаем JS файл
        .pipe(gulp.dest('app/js')); // Выгружаем в папку app/js
});

gulp.task('code', function () {
    return gulp.src('app/*.html')
        .pipe(browserSync.reload({stream: true}))
});

gulp.task('css-libs', function () {
    return gulp.src([
        'app/css/normalize.css',
        'app/libs/jquery-nice-select-1.1.0/css/nice-select.css',
        'app/libs/air-datepicker/dist/css/datepicker.min.css'
    ]) // Выбираем файл для минификации
        .pipe(sass()) // Преобразуем sass в CSS посредством gulp-sass
        .pipe(cssnano()) // Сжимаем
        .pipe(concat('libs.min.css'))
        .pipe(gulp.dest('app')); // Выгружаем в папку app/css
});

gulp.task('clean', done => {
    return del.sync('dist'); // Удаляем папку dist перед сборкой
    done();
});

gulp.task('img', function () {
    return gulp.src('app/img/**/*') // Берем все изображения из app
        .pipe(imagemin({ // С кешированием
            // .pipe(imagemin({ // Сжимаем изображения без кеширования
            interlaced: true,
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngquant()]
        }))/**/
        .pipe(gulp.dest('dist/img')); // Выгружаем на продакшен

});

gulp.task('prebuild', done => {

    var buildCss = gulp.src([ // Переносим библиотеки в продакшен
        'app/main.css',
        'app/libs.min.css'
    ])
        .pipe(gulp.dest('dist'))

    var buildFonts = gulp.src('app/fonts/**/*') // Переносим шрифты в продакшен
        .pipe(gulp.dest('dist/fonts'))

    var buildJs = gulp.src('app/js/**/*') // Переносим скрипты в продакшен
        .pipe(gulp.dest('dist/js'))

    var buildHtml = gulp.src('app/*.html') // Переносим HTML в продакшен
        .pipe(gulp.dest('dist'));

    var buildHtmlPages = gulp.src('app/pages/*.html') // Переносим HTML в продакшен
        .pipe(gulp.dest('dist/pages'));
    done();

});

gulp.task('clear', done => {
    return cache.clearAll();
    done();
})

gulp.task('watch', function () {
    gulp.watch('app/sass/**/*.scss', gulp.parallel('sass')); // Наблюдение за sass файлами
    gulp.watch('app/*.html', gulp.parallel('code')); // Наблюдение за HTML файлами в корне проекта
    gulp.watch(['app/js/common.js', 'app/libs/**/*.js'], gulp.parallel('scripts')); // Наблюдение за главным JS файлом и за библиотеками
});
gulp.task('default', gulp.parallel('css-libs', 'sass', 'scripts', 'browser-sync', 'watch'));
gulp.task('build', gulp.parallel('clean', 'prebuild', 'img'));