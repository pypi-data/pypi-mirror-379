# Licensed under the Apache License, Version 2.0 (the "License");
# Adapted from VoxCPM for TTS WebUI project, switched ASR to Whisper

import os
import numpy as np
import torch
import gradio as gr  
from typing import Optional, Tuple

import voxcpm


class VoxCPMDemo:
    def __init__(self) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"🚀 Running on device: {self.device}")

        self.voxcpm_model: Optional[voxcpm.VoxCPM] = None
        self.default_local_model_dir = "./data/models/voxcpm/VoxCPM-0.5B"

    # ---------- Model helpers ----------
    def _resolve_model_dir(self) -> str:
        if os.path.isdir(self.default_local_model_dir):
            return self.default_local_model_dir

        repo_id = "openbmb/VoxCPM-0.5B"
        if len(repo_id) > 0:
            target_dir = self.default_local_model_dir
            if not os.path.isdir(target_dir):
                try:
                    from huggingface_hub import snapshot_download  # type: ignore
                    os.makedirs(target_dir, exist_ok=True)
                    print(f"Downloading model from HF repo '{repo_id}' to '{target_dir}' ...")
                    snapshot_download(repo_id=repo_id, local_dir=target_dir, local_dir_use_symlinks=False)
                except Exception as e:
                    print(f"Warning: HF download failed: {e}. Falling back to 'data'.")
                    return "models"
            return target_dir
        return "models"

    def get_or_load_voxcpm(self) -> voxcpm.VoxCPM:
        if self.voxcpm_model is not None:
            return self.voxcpm_model
        print("Model not loaded, initializing...")
        model_dir = self._resolve_model_dir()
        print(f"Using model dir: {model_dir}")
        self.voxcpm_model = voxcpm.VoxCPM(voxcpm_model_path=model_dir, zipenhancer_model_path="iic/speech_zipenhancer_ans_multiloss_16k_base", enable_denoiser=True, optimize=False)
        print("Model loaded successfully.")
        return self.voxcpm_model

    # ---------- Functional endpoints ----------
    def prompt_wav_recognition(self, prompt_wav: Optional[str]) -> str:
        from extensions.builtin.extension_whisper.main import transcribe
        if prompt_wav is None:
            return ""
        result = transcribe(prompt_wav)
        return result

    def generate_tts_audio(
        self,
        text_input: str,
        prompt_wav_path_input: Optional[str] = None,
        prompt_text_input: Optional[str] = None,
        cfg_value_input: float = 2.0,
        inference_timesteps_input: int = 10,
        do_normalize: bool = True,
        denoise: bool = True,
    ) -> Tuple[int, np.ndarray]:
        """
        Generate speech from text using VoxCPM; optional reference audio for voice style guidance.
        Returns (sample_rate, waveform_numpy)
        """
        current_model = self.get_or_load_voxcpm()

        text = (text_input or "").strip()
        if len(text) == 0:
            raise ValueError("Please input text to synthesize.")

        prompt_wav_path = prompt_wav_path_input if prompt_wav_path_input else None
        prompt_text = prompt_text_input if prompt_text_input else None

        print(f"Generating audio for text: '{text[:60]}...'")
        wav = current_model.generate(
            text=text,
            prompt_text=prompt_text,
            prompt_wav_path=prompt_wav_path,
            cfg_value=float(cfg_value_input),
            inference_timesteps=int(inference_timesteps_input),
            normalize=do_normalize,
            denoise=denoise,
        )
        return (16000, wav)


# ---------- UI Builders ----------

def create_demo_interface(demo: VoxCPMDemo):
    """Build the Gradio UI for VoxCPM demo."""
    # Quick Start
    with gr.Accordion("📋 Quick Start Guide ｜快速入门", open=False, elem_id="acc_quick"):
        gr.Markdown("""
        ### How to Use ｜使用说明
        1. **(Optional) Provide a Voice Prompt** - Upload or record an audio clip to provide the desired voice characteristics for synthesis.  
            **（可选）提供参考声音** - 上传或录制一段音频，为声音合成提供音色、语调和情感等个性化特征
        2. **(Optional) Enter prompt text** - If you provided a voice prompt, enter the corresponding transcript here (auto-recognition available).  
            **（可选项）输入参考文本** - 如果提供了参考语音，请输入其对应的文本内容（支持自动识别）。
        3. **Enter target text** - Type the text you want the model to speak.  
            **输入目标文本** - 输入您希望模型朗读的文字内容。
        4. **Generate Speech** - Click the "Generate" button to create your audio.  
            **生成语音** - 点击"生成"按钮，即可为您创造出音频。
        """)

    # Pro Tips
    with gr.Accordion("💡 Pro Tips ｜使用建议", open=False, elem_id="acc_tips"):
        gr.Markdown("""
        ### Prompt Speech Enhancement｜参考语音降噪
        - **Enable** to remove background noise for a clean, studio-like voice, with an external ZipEnhancer component.  
            **启用**：通过 ZipEnhancer 组件消除背景噪音，获得更好的音质。
        - **Disable** to preserve the original audio's background atmosphere.  
            **禁用**：保留原始音频的背景环境声，如果想复刻相应声学环境。

        ### Text Normalization｜文本正则化
        - **Enable** to process general text with an external WeTextProcessing component.  
            **启用**：使用 WeTextProcessing 组件，可处理常见文本。
        - **Disable** to use VoxCPM's native text understanding ability. For example, it supports phonemes input ({HH AH0 L OW1}), try it!  
            **禁用**：将使用 VoxCPM 内置的文本理解能力。如，支持音素输入（如 {da4}{jia1}好）和公式符号合成，尝试一下！

        ### CFG Value｜CFG 值
        - **Lower CFG** if the voice prompt sounds strained or expressive.  
            **调低**：如果提示语音听起来不自然或过于夸张。
        - **Higher CFG** for better adherence to the prompt speech style or input text.  
            **调高**：为更好地贴合提示音频的风格或输入文本。

        ### Inference Timesteps｜推理时间步
        - **Lower** for faster synthesis speed.  
            **调低**：合成速度更快。
        - **Higher** for better synthesis quality.  
            **调高**：合成质量更佳。
        """)

    # Main controls
    with gr.Row():
        with gr.Column():
            prompt_wav = gr.Audio(
                sources=["upload", 'microphone'],
                type="filepath",
                label="Prompt Speech (Optional, or let VoxCPM improvise)",
            )
            DoDenoisePromptAudio = gr.Checkbox(
                value=False,
                label="Prompt Speech Enhancement",
                elem_id="chk_denoise",
                info="We use ZipEnhancer model to denoise the prompt audio."
            )
            with gr.Row():
                prompt_text = gr.Textbox(
                    label="Prompt Text",
                    placeholder="Please enter the prompt text. Automatic recognition is supported, and you can correct the results yourself..."
                )
            run_btn = gr.Button("Generate Speech", variant="primary")

        with gr.Column():
            cfg_value = gr.Slider(
                minimum=1.0,
                maximum=3.0,
                value=2.0,
                step=0.1,
                label="CFG Value (Guidance Scale)",
                info="Higher values increase adherence to prompt, lower values allow more creativity"
            )
            inference_timesteps = gr.Slider(
                minimum=4,
                maximum=30,
                value=10,
                step=1,
                label="Inference Timesteps",
                info="Number of inference timesteps for generation (higher values may improve quality but slower)"
            )
            with gr.Row():
                text = gr.Textbox(
                    label="Target Text",
                )
            with gr.Row():
                DoNormalizeText = gr.Checkbox(
                    value=False,
                    label="Text Normalization",
                    elem_id="chk_normalize",
                    info="We use wetext library to normalize the input text."
                )
            audio_output = gr.Audio(label="Output Audio")

    # Wiring
    run_btn.click(
        fn=demo.generate_tts_audio,
        inputs=[text, prompt_wav, prompt_text, cfg_value, inference_timesteps, DoNormalizeText, DoDenoisePromptAudio],
        outputs=[audio_output],
        show_progress=True,
        api_name="generate",
    )
    prompt_wav.change(fn=demo.prompt_wav_recognition, inputs=[prompt_wav], outputs=[prompt_text])




if __name__ == "__main__":
    demo = VoxCPMDemo()
    with gr.Blocks() as interface:
        create_demo_interface(demo)
    interface.launch()
