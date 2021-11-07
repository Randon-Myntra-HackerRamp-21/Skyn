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

export const putForm = ({features, currType, currTone, navigate}) => {
fetch("/recommend", {
        method: "put",
        headers: {
            "Content-Type": "application/json",

        },
        body: JSON.stringify({ "features": features, "type":currType, "tone":currTone})
    })
    .then(res => res.json())
    .then(data => {

        if (data.error) {
            console.log("Error")
        }
        else {
            navigate("/recs")
            console.log(data)
        }
    }).catch(err => {
        console.log(err)
    })
}