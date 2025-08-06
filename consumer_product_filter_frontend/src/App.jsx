import React, { useState } from 'react'
import './App.css'

function App() {
  const [selectedImage, setSelectedImage] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [analysisResult, setAnalysisResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleImageChange = (event) => {
    const file = event.target.files[0]
    if (file) {
      setSelectedImage(file)
      const reader = new FileReader()
      reader.onload = (e) => setImagePreview(e.target.result)
      reader.readAsDataURL(file)
      setAnalysisResult(null)
      setError(null)
    }
  }

  const analyzeImage = async () => {
    if (!selectedImage) {
      setError('Lütfen önce bir görsel seçin.')
      return
    }

    setLoading(true)
    setError(null)

    const formData = new FormData()
    formData.append('image', selectedImage)

    try {
      const response = await fetch('http://localhost:5002/api/analyze_image_only', {
        method: 'POST',
        body: formData,
      })

      console.log('Response status:', response.status)
      console.log('Response headers:', response.headers)

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ error: 'Unknown error' }))
        throw new Error(`Sunucu hatası: ${response.status} - ${errorData.error || 'Bilinmeyen hata'}`)
      }

      const result = await response.json()
      setAnalysisResult(result)
    } catch (error) {
      console.error('Analiz hatası:', error)
      setError(`Analiz sırasında hata oluştu: ${error.message}`)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-blue-50 to-teal-50">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="header-section">
          <h1 className="main-title">
            HealthyLife AI
          </h1>
          <p className="subtitle">
            📷 Ürün etiketlerinizi analiz ederek sağlıklı yaşam tercihlerinizi destekliyoruz
          </p>
        </div>

        <div className="main-grid">
          {/* Sol Panel - Görsel Yükleme */}
          <div className="card">
            <h2 className="card-title">📱 Ürün Etiketi Yükle</h2>

            <div className="upload-area">
              <input
                type="file"
                accept="image/*"
                onChange={handleImageChange}
                className="hidden"
                id="image-upload"
              />
              <label htmlFor="image-upload" className="cursor-pointer">
                <div className="upload-icon">
                  <svg className="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                  </svg>
                </div>
                <p className="upload-text">🖱️ Ürün etiketi fotoğrafını seçin</p>
                <p className="upload-subtext">JPG, PNG veya GIF formatında</p>
              </label>
            </div>

            {imagePreview && (
              <div className="image-preview">
                <h3 className="preview-title">🖼️ Seçilen Görsel:</h3>
                <img 
                  src={imagePreview} 
                  alt="Seçilen görsel" 
                  className="preview-image"
                />
              </div>
            )}

            <button
              onClick={analyzeImage}
              disabled={!selectedImage || loading}
              className="analyze-button"
            >
              {loading ? (
                <>
                  <div className="spinner"></div>
                  🔄 Analiz Ediliyor...
                </>
              ) : (
                '🧠 AI ile Analiz Et'
              )}
            </button>
          </div>

          {/* Sağ Panel - Analiz Sonuçları */}
          <div className="card">
            <h2 className="card-title">📊 Analiz Sonuçları</h2>

            {error && (
              <div className="error-message">
                <span className="error-icon">⚠️</span>
                <p className="error-text">{error}</p>
              </div>
            )}

            {analysisResult ? (
              <div className="results-section">
                <div className="analysis-result">
                  <h3 className="analysis-title">🤖 AI Analizi</h3>
                  <div className="analysis-content">
                    <p className="analysis-text">
                      {analysisResult.analysis}
                    </p>
                  </div>
                </div>

                {analysisResult.confidence_score && (
                  <div className="confidence-score">
                    <span className="confidence-label">🎯 Güven Skoru:</span>
                    <span className="confidence-value">
                      %{Math.round(analysisResult.confidence_score * 100)}
                    </span>
                  </div>
                )}
              </div>
            ) : (
              <div className="empty-state">
                <div className="empty-icon">🔍</div>
                <p className="empty-title">Analiz sonuçları burada görünecek</p>
                <p className="empty-subtitle">Önce bir ürün etiketi fotoğrafı yükleyin</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
