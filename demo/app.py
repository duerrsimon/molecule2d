
import gradio as gr
from gradio_molecule2d import Molecule2D


example = Molecule2D().example_inputs()

with gr.Blocks() as demo:
    Molecule2D(value=example, interactive=True)
    Molecule2D(value=example, interactive=False)


demo.launch()
