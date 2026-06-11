import { beforeEach, describe, expect, it } from 'vitest'

import { useFavorites } from '@/composables/useFavorites'
import type { MovieListItem } from '@/types'

const sampleMovie: MovieListItem = {
  id: 1,
  title: 'Inception',
  release_year: 2010,
  rating: 8.8,
  director: { id: 1, name: 'Christopher Nolan' },
  genres: [{ id: 1, name: 'Sci-Fi' }],
}

describe('useFavorites', () => {
  beforeEach(() => {
    localStorage.clear()
  })

  it('starts with an empty favorites list', () => {
    const { favorites } = useFavorites()
    expect(favorites.value).toEqual([])
  })

  it('adds and removes favorites', () => {
    const { favorites, isFavorite, toggleFavorite } = useFavorites()

    toggleFavorite(sampleMovie)
    expect(isFavorite(1)).toBe(true)
    expect(favorites.value).toHaveLength(1)

    toggleFavorite(sampleMovie)
    expect(isFavorite(1)).toBe(false)
    expect(favorites.value).toHaveLength(0)
  })

  it('persists favorites to local storage', () => {
    const { toggleFavorite } = useFavorites()
    toggleFavorite(sampleMovie)

    const stored = JSON.parse(localStorage.getItem('movie-explorer-favorites') || '[]') as MovieListItem[]
    expect(stored[0].title).toBe('Inception')
  })
})
