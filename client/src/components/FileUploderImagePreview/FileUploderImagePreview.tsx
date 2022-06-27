import React from "react"
import "./FileUploaderImagePreview.css"

interface IProps {
    imageSrc: string
}


export default function FileUploaderImagePreview(props: IProps) {
    const { imageSrc } = props;

    return (
        <div>
            {<img className={"image-preview"} src={imageSrc} alt={imageSrc} key={imageSrc}/>}
        </div>
    )
}