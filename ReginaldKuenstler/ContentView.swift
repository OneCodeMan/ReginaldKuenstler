//
//  ContentView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-15.
//

import SwiftUI
import SwiftVibrantium

struct ContentView: View {
    @State var rectColour = Color(UIColor.red)
    var body: some View {
        VStack {
            VStack {
                
            }
            .frame(width: 100, height: 50)
            .background(rectColour)
        }
        .padding()
        .onAppear {
            let vm = KuenstlerViewModel()
            let imgTitle = "Starry Night"
            let imgName = "starz"
            let image = UIImage(named: imgName)!
            let artwork = Artwork(image: image, title: imgTitle)
            vm.performAnalOnImage(artwork: artwork)
        }
    }
}

#Preview {
    ContentView()
}

struct Artwork {
    var image: UIImage
    var title: String
}

struct Palette {
    var colours: [String] = []
}

class KuenstlerViewModel {
    
    func performAnalOnImage(artwork: Artwork) {
        print("performing anal on \(artwork.title)")
        Vibrant.from(artwork.image).getPalette() { palette in
            let p = palette
            let vibrant = p.Vibrant?.hex
            let darkVibrant = p.DarkVibrant?.hex
            let lightVibrant = p.LightVibrant?.hex
            let mutedVibrant = p.Muted?.hex
            let lightMuted = p.LightMuted?.hex
            let darkMuted = p.DarkMuted?.hex
            print("vibrant: \(vibrant);\n darkvibrant: \(darkVibrant);\n lightVibrant: \(lightVibrant); mutedVibrant: \(mutedVibrant); lightMuted: \(lightMuted); darkMuted: \(darkMuted)")
        }
    }
}
