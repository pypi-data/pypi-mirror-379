import gradio as gr


def vox_cpm_ui():
    from .ui import VoxCPMDemo, create_demo_interface
    demo = VoxCPMDemo()
    create_demo_interface(demo)


def extension__tts_generation_webui():
    vox_cpm_ui()
    
    return {
        "package_name": "tts_webui_extension.vox_cpm",
        "name": "VoxCPM",
        "requirements": "git+https://github.com/rsxdalv/tts_webui_extension.vox_cpm@main",
        "description": "A template extension for TTS Generation WebUI",
        "extension_type": "interface",
        "extension_class": "text-to-speech",
        "author": "OpenBMB",
        "extension_author": "rsxdalv",
        "license": "MIT",
        "website": "https://github.com/rsxdalv/tts_webui_extension.vox_cpm",
        "extension_website": "https://github.com/rsxdalv/tts_webui_extension.vox_cpm",
        "extension_platform_version": "0.0.1",
    }


if __name__ == "__main__":
    if "demo" in locals():
        locals()["demo"].close()
    with gr.Blocks() as demo:
        with gr.Tab("Vox cpm", id="vox_cpm"):
            vox_cpm_ui()

    demo.launch(
        server_port=7772,  # Change this port if needed
    )
