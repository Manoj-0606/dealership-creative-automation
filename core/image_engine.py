import os
from PIL import Image

class ImageEngine:
    def __init__(self, assets_path="assets", output_path="output"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.assets_path = os.path.join(base_dir, assets_path)
        self.output_path = os.path.join(base_dir, output_path)

        self.input_path = os.path.join(self.assets_path, "Sample-input-images")
        self.logo_path = os.path.join(self.assets_path, "Logos")
        self.panel_path = os.path.join(self.assets_path, "Dealership-panels")

        os.makedirs(self.output_path, exist_ok=True)

    def load_logo(self):
        logos = [f for f in os.listdir(self.logo_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        if not logos:
            return None
        return Image.open(os.path.join(self.logo_path, logos[0])).convert("RGBA")

    def load_panels(self):
        panels = []
        for root, _, files in os.walk(self.panel_path):
            for f in files:
                if f.lower().endswith((".png", ".jpg", ".jpeg")):
                    panels.append(Image.open(os.path.join(root, f)).convert("RGBA"))
        return panels

    def process_image(self, image_path, logo, panel):
        base = Image.open(image_path).convert("RGBA")
        bw, bh = base.size

        if panel:
            panel_resized = panel.resize((bw, int(bh * 0.3)))
            panel_resized.putalpha(180)
            base.paste(panel_resized, (0, bh - panel_resized.size[1]), panel_resized)

        if logo:
            lw, lh = logo.size
            scale = min((bw * 0.15) / lw, (bh * 0.15) / lh)
            new_size = (int(lw * scale), int(lh * scale))
            logo_resized = logo.resize(new_size)

            position = (bw - new_size[0] - 30, 30)
            base.paste(logo_resized, position, logo_resized)

        return base.convert("RGB")

    def run(self):
        print("Starting processing...")

        logo = self.load_logo()
        panels = self.load_panels()

        files = [f for f in os.listdir(self.input_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

        for i, file in enumerate(files):
            print(f"Processing: {file}")

            input_file = os.path.join(self.input_path, file)
            panel = panels[i % len(panels)] if panels else None

            output_img = self.process_image(input_file, logo, panel)

            name, _ = os.path.splitext(file)
            output_file = os.path.join(self.output_path, f"{name}_output.jpg")
            output_img.save(output_file)

        print("Finished processing.")