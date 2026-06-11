import type {
  ActorDetail,
  ActorListItem,
  ApiError,
  DirectorDetail,
  DirectorListItem,
  GenreListResponse,
  MovieDetail,
  MovieListResponse,
} from '@/types'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

async function request<T>(path: string, params?: Record<string, string | number>): Promise<T> {
  const url = new URL(`${API_URL}${path}`)
  if (params) {
    Object.entries(params).forEach(([key, value]) => {
      if (value !== '' && value !== null && value !== undefined) {
        url.searchParams.set(key, String(value))
      }
    })
  }

  const response = await fetch(url.toString())
  if (!response.ok) {
    const error = (await response.json().catch(() => ({ detail: response.statusText }))) as ApiError
    throw new Error(error.detail || 'Request failed')
  }
  return response.json() as Promise<T>
}

export const api = {
  getMovies(filters: {
    genre?: string
    director?: string
    year?: string
    actor?: string
  } = {}): Promise<MovieListResponse> {
    return request<MovieListResponse>('/movies', filters)
  },

  getMovie(id: number): Promise<MovieDetail> {
    return request<MovieDetail>(`/movies/${id}`)
  },

  getActors(filters: { movie?: string; genre?: string } = {}): Promise<{
    items: ActorListItem[]
    total: number
  }> {
    return request('/actors', filters)
  },

  getActor(id: number): Promise<ActorDetail> {
    return request<ActorDetail>(`/actors/${id}`)
  },

  getDirectors(): Promise<{ items: DirectorListItem[]; total: number }> {
    return request('/directors')
  },

  getDirector(id: number): Promise<DirectorDetail> {
    return request<DirectorDetail>(`/directors/${id}`)
  },

  getGenres(): Promise<GenreListResponse> {
    return request<GenreListResponse>('/genres')
  },
}
