import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import MovieDetailView from '@/views/MovieDetailView'
import CommentCreateView from '@/views/CommentCreateView'
import CommentDetailView from '@/views/CommentDetailView'
import CommentUpdateView from '@/views/CommentUpdateView'
import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'
import UserStatusView from '@/views/UserStatusView'
import FourZeroFourView from '@/views/FourZeroFourView'

import RecommendView from '@/views/RecommendView'
import PopularityView from '@/views/PopularityView'
import AverageView from '@/views/AverageView'
import RandomView from '@/views/RandomView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
    
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/UserStatus',
    name: 'UserStatusView',
    component: UserStatusView
  },
  {
    path: '/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/:id/create',
    name: 'CommentCreateView',
    component: CommentCreateView
  },
  {
    path: '/:id/detail/:pk',
    name: 'CommentDetailView',
    component: CommentDetailView
  },
  {
    path: '/:id/update/:pk',
    name: 'CommentUpdateView',
    component: CommentUpdateView
  },
  //////////////// 영화추천 router ////////////////////////
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView,
    children: [
      // 인기순
      {
        path: '/recommend/popularity',
        name: 'PopularityView',
        component: PopularityView
      },
      // 평점순
      {
        path: '/recommend/average',
        name: 'AverageView',
        component: AverageView
      },
      //랜덤
      {
        path: '/recommend/random',
        name: 'RandomView',
        component: RandomView
      },
    ]
  },
  //404//
  {
    path: '*',
    name: 'FourZeroFourView',
    component: FourZeroFourView,
    // redirect: 'FourZeroFourView'

    // redirect: '/404'
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
