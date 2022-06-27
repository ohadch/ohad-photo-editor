import React from 'react';
import {useDropzone} from 'react-dropzone';
import "./FileUploader.css"

const SERVER_HOST = "http://localhost:8000/"

interface IProps {
    setImgSrc: (imgSrc: string | undefined) => void
    setFile: (file: any) => void
}

export default function FileUploader(props: IProps) {
    const { setImgSrc, setFile } = props

    const {getRootProps, getInputProps} = useDropzone({
        multiple: false,
        accept: {
            'image/*': []
        },
        onDrop: async (acceptedFiles: File[]) => {
            // Update the preview
            const fileToSet = acceptedFiles.map(file => Object.assign(file, {
                preview: URL.createObjectURL(file)
            }))[0]
            setFile(fileToSet)

            // Upload the file to the server
            const formData = new FormData();
            formData.append('file', acceptedFiles[0]);
            fetch(`${SERVER_HOST}upload`, {
                method: 'POST',
                body: formData
            })
                .then(response => response.blob())
                .then(blob => setImgSrc(URL.createObjectURL(blob)))

        }
    });


    return (
        <section className="container">
            <div {...getRootProps({className: 'dropzone'})} className={"dropzone"}>
                <input {...getInputProps()} />
                <p>Drag 'n' drop some files here, or click to select files</p>
            </div>
        </section>
    );
}