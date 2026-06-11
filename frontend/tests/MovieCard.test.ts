import { mount } from '@vue/test-utils'
import { describe, expect, it } from 'vitest'
import { createRouter, createWebHistory } from 'vue-router'

import MovieCard from '@/components/MovieCard.vue'
import type { MovieListItem } from '@/types'

const movie: MovieListItem = {
  id: 2,
  title: 'Dune',
  release_year: 2021,
  rating: 8.0,
  director: { id: 4, name: 'Denis Villeneuve' },
  genres: [{ id: 3, name: 'Sci-Fi' }],
}

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: { template: '<div />' } },
    { path: '/movies/:id', name: 'movie-detail', component: { template: '<div />' } },
    { path: '/directors/:id', name: 'director-detail', component: { template: '<div />' } },
  ],
})

describe('MovieCard', () => {
  it('renders movie details', async () => {
    const wrapper = mount(MovieCard, {
      props: { movie },
      global: {
        plugins: [router],
      },
    })

    await router.isReady()

    expect(wrapper.text()).toContain('Dune')
    expect(wrapper.text()).toContain('Denis Villeneuve')
    expect(wrapper.text()).toContain('Sci-Fi')
  })
})
