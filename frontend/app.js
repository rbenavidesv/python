new Vue({
    el: '#app',

    data () {
        return {
            name: 'Bitcoin',
            img: 'https://cryptologos.cc/logos/bitcoin-btc-logo.png',
            changepercent: -2,
            prices: [8400,7900,8200,9000,9400,11000,12000],
            pricesWithDays: [
                {day: 'Lunes', value: 8400},
                {day: 'Martes', value: 7900},
                {day: 'Miercoles', value: 8200},
                {day: 'Jueves', value: 9000},
                {day: 'Viernes', value: 9400},
                {day: 'Sabado', value: 11000},
                {day: 'Domingo', value: 12000},
            ]
        }
    }
})