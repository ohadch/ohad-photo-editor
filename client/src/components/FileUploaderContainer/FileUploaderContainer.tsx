import React, {useState} from "react"

import "./FileUploaderContainer.css"

import FileUploader from "../FileUploader/FileUploader";
import FileUploaderImagePreview from "../FileUploderImagePreview/FileUploderImagePreview";

export default function FileUploaderContainer() {
    const [imgSrc, setImgSrc] = useState<string | undefined>();
    const [file, setFile] = useState<any>();

    return (
        <div>
            <FileUploader setFile={setFile} setImgSrc={setImgSrc} />
            <div className={"preview-container"}>
                {file?.preview && <FileUploaderImagePreview imageSrc={file.preview}/>}
                {imgSrc && <FileUploaderImagePreview imageSrc={imgSrc}/>}
            </div>
        </div>
    )
}