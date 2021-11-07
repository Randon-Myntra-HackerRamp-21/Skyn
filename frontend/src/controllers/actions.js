export const UploadImage = (imageSrc, navigate) => {
    const data = new FormData()
    data.append("file", imageSrc)
    fetch("upload", {
        method: "put",
        body: data
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            console.log("Please add a photograph")
        }
        else {
            navigate("/form")
            console.log("All fin")
        }
    })
    .catch(err => {
        console.log(err.message)
    })
}