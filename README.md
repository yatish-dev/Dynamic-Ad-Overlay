Dynamic Ad Overlay (Live Geolocated Video Ads)

This project demonstrates a dynamic, location-based ad overlay system using computer vision. It detects green-marked areas in a webcam feed (e.g., product wrappers, posters) and replaces them with regional advertisement content based on the viewer's IP location.

🚀 Features

🌍 Location-aware ad delivery using IP geolocation

🟩 Green screen detection and replacement

🎥 Real-time webcam video processing

📦 Easy asset management for regional ads

📌 Fully open-source and demo-ready

🧠 How It Works

Detect viewer's location using IP (via ipinfo.io)

Map country code to a product image

Open webcam feed using OpenCV

Detect green area in frame using HSV masking

Replace the green-marked product area with a region-specific ad

🗂️ File Structure

dynamic_ad_overlay/<br>
├── main.py<br>
├── assets/<br>
│   └── product_images/<br>
│       ├── india_coconut.png<br>
│       ├── usa_orange.png<br>
│       ├── pakistan_mango.png<br>
│       ├── bangladesh_jackfruit.png<br>
│       ├── nigeria_peanut.png<br>
│       ├── uk_hazelnut.png<br>
│       └── default.png<br>

▶️ Getting Started

1. Clone the repository

git clone https://github.com/yatish-dev/dynamic-ad-overlay.git
cd dynamic-ad-overlay

2. Install dependencies

pip install opencv-python numpy requests

3. Run the live demo

python main.py

🟢 Make sure your product/wrapper has a green screen section in front of the webcam.

🔴 Press q to exit.

🌐 Supported Regions (default mapping)

Country

Product Image

IN 🇮🇳

india_coconut.png

US 🇺🇸

usa_orange.png

PK 🇵🇰

pakistan_mango.png

BD 🇧🇩

bangladesh_jackfruit.png

NG 🇳🇬

nigeria_peanut.png

UK 🇬🇧

uk_hazelnut.png

Add your own by editing the location_map dictionary in main.py.

📌 Use Cases

Influencer product placements

Location-sensitive ads in YouTube/Instagram videos

Stadium digital hoardings or green-screen billboards

E-commerce platform smart targeting

🧩 Future Enhancements

Multiple green zone detection

Audio variation based on location

Cloud SDK for platforms to embed

Chrome extension or OBS plugin integration

🛡️ License / Notice

This is a research and demo project. Patent pending. For demo/product pilot purposes only.

🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

## 📬 Contact  
Created by [Your Name] — [🔗 LinkedIn Profile]([https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/yatish-jobanputra-711468362/)) · [✉️ Email Me](mailto:yatishjobanputra@outlook.com)

For business/partnership inquiries, reach out with the subject line: `Dynamic Ad Overlay Collaboration`
