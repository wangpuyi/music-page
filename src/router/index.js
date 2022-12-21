import { createRouter,createWebHashHistory } from "vue-router"
import A from "../views/A"


const routes = [
    {
        path:"/A",
        component:A,
        children:[
            {path:'3',
            component:()=>import('../views/C.vue')
            },
            {
                path:'4',
                component:()=>import('../views/D.vue')
            }
            ]
    },
    {
        path:"/B",
        component:()=>import('../views//Ge-danneibu')
    },
    {
        path:"/C",
        component:()=>import('../views/C')
    },
    {
        path:"/Ge-dan",
        component:()=>import('../views/Ge-dan')
    },
    {
        path:"/Ge-qujiemian",
        component:()=>import('../views/Ge-qujiemian')
    },

    

]

const router=createRouter({
    history:createWebHashHistory(),
    routes


})

export default router;