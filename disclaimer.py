with gr.Box(visible=is_spaces):
    if(is_spaces and is_shared_ui):
        gr.HTML(f'''  
        <div>
            <p>🚧 Use of this beta version of our software is subject to and governed by our beta software policy. Click here to view</p>
        </div>
        ''')
    elif(is_spaces):
        import torch
        if(not torch.cuda.is_available()):
            gr.HTML(f'''  
            <div>
                <p>🚧 Use of this beta version of our software is subject to and governed by our beta software policy. Click here to view</p>
            </div>
            ''')
        else:
            gr.HTML(f'''  
            <div>
                <p>🚧 Use of this beta version of our software is subject to and governed by our beta software policy. Click here to view</p>
            </div>
            ''')
