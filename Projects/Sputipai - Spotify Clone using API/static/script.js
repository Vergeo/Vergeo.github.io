document.addEventListener("DOMContentLoaded", () => {

    const apikey = "mpQBYk8tyzQ87Ig5aesHeRNz3pYdylLq";

    document.querySelector(".new-profile-btn").onclick = function() {
        document.querySelector(".new-search").style.display = "flex";
        document.querySelector(".new-search").style.animation = "newProfileAnimation 0.3s linear";
        document.querySelector(".profile-entry").value = "";
    }

    document.querySelector(".recommended").onclick = function() {
        document.querySelector(".content").style.display = "block";
    }
    
    document.querySelector(".search-track").onclick = function() {
        document.querySelector(".new-search-h1").innerHTML = "Insert Track ID"
        document.querySelector(".new-search").style.display = "flex";
        document.querySelector(".new-search").style.animation = "newProfileAnimation 0.3s linear";
        document.querySelector(".profile-entry").value = "";
    }

    document.querySelector(".search-playlist").onclick = function() {
        document.querySelector(".new-search-h1").innerHTML = "Insert Playlist ID"
        document.querySelector(".new-search").style.display = "flex";
        document.querySelector(".new-search").style.animation = "newProfileAnimation 0.3s linear";
        document.querySelector(".profile-entry").value = "";
    }

    document.querySelector(".search-profile").onclick = function() {
        document.querySelector(".new-search-h1").innerHTML = "Insert User ID"
        document.querySelector(".new-search").style.display = "flex";
        document.querySelector(".new-search").style.animation = "newProfileAnimation 0.3s linear";
        document.querySelector(".profile-entry").value = "";
    }

    var recommend_playlist = [
        "7KGyS7ifcoQrmNscH1x5zW",
        "3FZKB81dSvBEvLUlqLmXyv",
        "37i9dQZF1E37jjKgICf1EE",
        "7tPHH6kZtiArzfOM1qcaaP",
        "7BG6JPYW5HuBRuwvp5H1LV",
        "45FqeWKiCv2wL7fnTuxj2y",
        "6jZqqk2mhMxEQqXNcpUaH5",
        "2fQwOcwBNIE2Yrh0kBbwMB",
        "6LTcKoH6RVeJqMc0MruvD2"
    ]

    function getPlaylistInfo(id, img, head) {
        const request = new XMLHttpRequest();
        request.onload = function() {
            const data = JSON.parse(this.responseText);

            // console.log(data);
            // console.log("Finished");
            if (img) {
                document.querySelector(img).src = data["images"][0]["url"];
            }
            if (head) {
                document.querySelector(head).innerHTML = data["name"];
            }
            
        }
    
        request.open("GET", `https://api.apilayer.com/spotify/playlist?id=${id}&apikey=${apikey}`);
        request.send();
        return false;
    }
    
    for (var i = 1; i <= 6; i++) {
        var item = recommend_playlist[Math.floor(Math.random()*recommend_playlist.length)];
        var index = recommend_playlist.indexOf(item);
        if (index > -1) {
            recommend_playlist.splice(index, 1);
        }
        getPlaylistInfo(item, `.rec-playlist-img-${i}`, `.rec-playlist-h-${i}`);
    }

    function findUser(id) {
        const request = new XMLHttpRequest();
        request.onload = function() {
            const data = JSON.parse(this.responseText);

            console.log(data);

        }
    
        request.open("GET", `https://api.apilayer.com/spotify/user_profile?id=${id}&apikey=${apikey}`);
        request.send();
        return false;
    }

    function findTrack(id) {
        const request = new XMLHttpRequest();
        request.onload = function() {
            const data = JSON.parse(this.responseText);

            console.log(data);
            document.querySelector(".track-img").src = data["tracks"][0]["album"]["images"][0]["url"];
            document.querySelector(".track-title").innerHTML = data["tracks"][0]["name"];
            document.querySelector(".track-artist").innerHTML = data["tracks"][0]["artists"][0]["name"];
            document.querySelector(".track-duration").innerHTML = "Duration : " + data["tracks"][0]["duration_ms"]+" ms";
            document.querySelector(".track-release-date").innerHTML = "Album Release Date : " + data["tracks"][0]["album"]["release_date"];
            document.querySelector(".track-id").innerHTML = "Track ID : " + data["tracks"][0]["id"];
            document.querySelector(".track-website").href = data["tracks"][0]["external_urls"]["spotify"];
            document.querySelector(".track-spotify").href = data["tracks"][0]["uri"];
        }
    
        request.open("GET", `https://api.apilayer.com/spotify/tracks?ids=${id}&apikey=${apikey}`);
        request.send();
        return false;
    }

    function findPlaylist(id) {
        const request = new XMLHttpRequest();
        request.onload = function() {
            const data = JSON.parse(this.responseText);

            document.querySelector(".playlist-img").src = data["images"][0]["url"];
            document.querySelector(".playlist-title").innerHTML = data["name"];
            document.querySelector(".playlist-owner").innerHTML = data["owner"]["display_name"];
            document.querySelector(".playlist-track-count").innerHTML = data["tracks"]["total"] + " songs";
            document.querySelector(".playlist-follower-count").innerHTML = data["followers"]["total"] + " likes";
            // document.querySelector("playlist-id")
            // document.querySelector("plalist-website").href =
            document.querySelector(".playlist-spotify").href = data["uri"]; 

            console.log(data);
            findPlaylistTracks(id);
        }
    
        request.open("GET", `https://api.apilayer.com/spotify/playlist?id=${id}&apikey=${apikey}`);
        request.send();

        return false;
    }

    function findPlaylistTracks(id) {
        request = new XMLHttpRequest();

        request.onload = function() {
            const data = JSON.parse(this.responseText);
            console.log(data);

            data["items"].forEach(song => {
                console.log(song);
                const a = document.createElement("a");
                const img = document.createElement("img");
                const title = document.createElement("p");
                const artist = document.createElement("p");
                a.href = song["track"]["uri"];
                img.src = song["track"]["album"]["images"][0]["url"];
                title.innerHTML = song["track"]["name"];
                artist.innerHTML = song["track"]["artists"][0]["name"];
                artist.class = "p-track-artist";
                a.append(img);
                a.append(title);
                a.append(artist);
                document.querySelector(".playlist-tracks").append(a);
            });
        }
    
        request.open("GET", `https://api.apilayer.com/spotify/playlist_tracks?id=${id}&apikey=${apikey}`);
        request.send();
        return false;
    }

    document.querySelector(".profile-submit").onclick = function() {
        document.querySelector(".new-search").style.display = "none";
        const res = document.querySelector(".profile-entry").value;

        if (document.querySelector(".new-search-h1").innerHTML == "Insert User ID") findUser(res);
        if (document.querySelector(".new-search-h1").innerHTML == "Insert Track ID") findTrack(res);
        if (document.querySelector(".new-search-h1").innerHTML == "Insert Playlist ID") findPlaylist(res);
    }

    document.querySelector(".profile-cancel").onclick = function() {
        document.querySelector(".new-search").style.display = "none";
    }
})