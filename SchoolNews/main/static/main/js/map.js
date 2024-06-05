ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
            center: [57.832998, 28.250481],
            zoom: 16
        }, {
            searchControlProvider: 'yandex#search'
        }),

        // Создаём макет содержимого.
        myPlacemark = new ymaps.Placemark(myMap.getCenter(), {
            hintContent: 'Школа',
            balloonContent: 'Школа'
        }, {
            iconLayout: 'default#image',
            iconImageHref: 'https://yastatic.net/mapsapi-icons/v2.5.2/icondd9914f1.png',
            iconImageSize: [30, 42],
            iconImageOffset: [-3, -42]
        });

    myMap.geoObjects
        .add(myPlacemark);
});