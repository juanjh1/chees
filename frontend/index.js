import Vue from "vue"


const aplication = 



new  Vue ( {
    el: '#app',
    data(){
        return {
            mensaje: 'hola cara de monda'
        }
    },

    template() {
        
        return `<div> hola mi vida, {{mensaje}}</div>`
        
    }
})


