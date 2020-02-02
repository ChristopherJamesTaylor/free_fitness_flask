import Vue from 'vue'
import Router from 'vue-router'

import {routes} from "@/router/routes"
import { checkAccessMiddleware} from "@/router/Middleware";

Vue.use(Router);

const router = new Router({
  routes,
});

router.beforeEach(checkAccessMiddleware);

export default router;