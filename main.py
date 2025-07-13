import cv2
import numpy as np
import requests
import os

# Mapping of country code to image and product name
location_map = {
    "in": ("india_coconut.png", "India", "Coconut Fizz"),
    "us": ("usa_orange.png", "United States", "Orange Zing"),
    "pk": ("pakistan_mango.png", "Pakistan", "Mango Burst"),
    "bd": ("bangladesh_jackfruit.png", "Bangladesh", "Jackfruit Joy"),
    "ng": ("nigeria_peanut.png", "Nigeria", "Peanut Splash"),
    "uk": ("uk_hazelnut.png", "United Kingdom", "Hazelnut Hype")
}
location_keys = list(location_map.keys())

def detect_country_by_ip():
    try:
        response = requests.get("https://ipinfo.io/json")
        return response.json().get("country", "in").lower()
    except:
        return "in"

def load_overlay_image(code):
    filename, _, _ = location_map.get(code, ("default.png", "Unknown", "Unknown Product"))
    path = os.path.join("assets", "product_images", filename)
    return cv2.imread(path)

def get_country_name(code):
    return location_map.get(code, ("default.png", "Unknown", "Unknown Product"))[1]

def get_product_name(code):
    return location_map.get(code, ("default.png", "Unknown", "Unknown Product"))[2]

def process_live_camera():
    current_country = detect_country_by_ip()
    overlay_img = load_overlay_image(current_country)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot access webcam")

    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    print("Press 0 to auto-detect region from IP")
    for i, code in enumerate(location_keys):
        print(f"{i+1}: {code.upper()} ({get_country_name(code)})")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_green, upper_green)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest)
            resized_overlay = cv2.resize(overlay_img, (w, h))
            roi = frame[y:y+h, x:x+w]
            mask_roi = mask[y:y+h, x:x+w]
            mask_inv = cv2.bitwise_not(mask_roi)

            bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
            fg = cv2.bitwise_and(resized_overlay, resized_overlay, mask=mask_roi)
            frame[y:y+h, x:x+w] = cv2.add(bg, fg)

        # Display info on frame
        country_text = f"Region: {current_country.upper()} - {get_country_name(current_country)}"
        product_text = f"Product: {get_product_name(current_country)}"

        cv2.putText(frame, country_text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.putText(frame, product_text, (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        cv2.putText(frame, "Press 1–6 to switch | 0 = Auto-detect | q = Quit", (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (180, 255, 180), 1)

        cv2.imshow("Live Ad Overlay", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('0'):
            current_country = detect_country_by_ip()
            overlay_img = load_overlay_image(current_country)
            print(f"Auto-detected: {current_country.upper()} ({get_country_name(current_country)})")
        elif ord('1') <= key <= ord(str(len(location_keys))):
            idx = key - ord('1')
            if 0 <= idx < len(location_keys):
                current_country = location_keys[idx]
                overlay_img = load_overlay_image(current_country)
                print(f"Switched to: {current_country.upper()} ({get_country_name(current_country)})")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_live_camera()
