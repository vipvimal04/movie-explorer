import { createRouter, createWebHistory } from 'vue-router'

import ActorDetailView from '@/views/ActorDetailView.vue'
import DirectorDetailView from '@/views/DirectorDetailView.vue'
import FavoritesView from '@/views/FavoritesView.vue'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/movies/:id', name: 'movie-detail', component: MovieDetailView, props: true },
    { path: '/actors/:id', name: 'actor-detail', component: ActorDetailView, props: true },
    { path: '/directors/:id', name: 'director-detail', component: DirectorDetailView, props: true },
    { path: '/favorites', name: 'favorites', component: FavoritesView },
  ],
})

export default router
