

export const routes = [

    {
        path: "/",
        name: "login",
        component: () =>
            import("@/components/login")
    },

    {   path: '/home',
        name: 'Home' ,
        component: () =>
            import("@/components/Home")
    },

    {   path: '/about',
        name: 'About',
        component: () =>
            import("@/components/About")
    },

    {   path: '/macros',
        name: 'Macros',
        component: () =>
            import("@/components/Macros")
    },

    {   path: '*',
        name: 'NotFound',
        component: () =>
            import("@/components/NotFound")
    },

    {   path: '/nutrition',
        name: 'Nutrition',
        component: () =>
            import("@/components/Nutrition")
    },

    {   path: '/tdee',
        name: 'TDEE',
        component: () =>
            import("@/components/TDEE")

    },

    {   path: '/gyms',
        name: 'Gym',
        component: () =>
            import("@/components/Gym")
    },

    {   path: '/fitnessplan',
        name: 'Fitness',
        component: () =>
            import("@/components/Fitness")
    },
    {
        path: "/registration",
        name: "registration",
        component: () =>
            import("@/components/Registration")
    },
    {
        path: "/profile",
        name: "profile",
        component: () =>
            import("@/components/Profile")
    },
    {
        path: "/currentfitnessplan",
        name: "currentfitnessplan",
        component: () =>
            import("@/components/CurrentFitnessPlan")
    },

]