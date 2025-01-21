import Viu from "./node_modules/viu"


const aplication = Viu()



const App = {
    data(){
        return {
            mensaje: 'hola cara de monda'
        }
    },

    template() {
        
        return `<div> hola mi vida, {{mensaje}}</div>`
        
    }
}

aplication.mount(App,'#app')
