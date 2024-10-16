//
//  ContentView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-15.
//

import SwiftUI
import SwiftVibrantium

struct ContentView: View {
    @State var imgTitle = ""
    @State var imgName = ""
    @State var infoString = ""
    var body: some View {
        VStack {
            VStack {
                Image(uiImage: UIImage(named: "calum")!)
                    .resizable()
                    .frame(width: 100, height: 300)
            }
            .frame(width: 250, height: 60)
            Text(infoString)
        }
        .padding()
        .onAppear {
            let vm = KuenstlerViewModel()
            self.imgTitle = "Calum from Aftersun"
            self.imgName = "calum"
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
        var infoString = ""
        print("performing anal on \(artwork.title)")
        Vibrant.from(artwork.image).getPalette() { palette in
            let p = palette
            let vibrant: String = p.Vibrant?.hex ?? ""
            let darkVibrant: String = p.DarkVibrant?.hex ?? ""
            let lightVibrant: String = p.LightVibrant?.hex ?? ""
            let mutedVibrant: String = p.Muted?.hex ?? ""
            let lightMuted: String = p.LightMuted?.hex ?? ""
            let darkMuted: String = p.DarkMuted?.hex ?? ""
            print("vibrant: \(vibrant);\n darkvibrant: \(darkVibrant);\n lightVibrant: \(lightVibrant); mutedVibrant: \(mutedVibrant); lightMuted: \(lightMuted); darkMuted: \(darkMuted)")
            
            // take input
            let inputs = [vibrant, darkVibrant, lightVibrant, mutedVibrant, lightMuted, darkMuted]
            var outputs: [VColour] = []
            
            let mapper = ColourMapper()
            let colourMap = mapper.createColourMapFromCSV()
            print("\n\n\n\n")
            
            
            // for every colour input
            for inputColour in inputs {
                // convert to rgb
                let rgbInputTuple = ColourConverter.hexToRGB(hex: inputColour)
                
                // calculate nearest distance, output
                let nearestColour = ColourConverter.findNearestColorFromRGBValue(rgbTuple: rgbInputTuple, colourMap: colourMap)
                outputs.append(nearestColour)
            }
            
            let inputOutputZip = zip(inputs, outputs)
            
            print("Analysis of \(artwork.title)")
            for (inputColour, outputColour) in inputOutputZip {
                let yap = "Vibrant took the input as \(inputColour), which corresponds to \(outputColour.name) (hex code: \(outputColour.hexCode))\n"
                infoString += yap
                print(yap)
            }
        }
        
        // convert the outputs to actual UIColours that u can use on a view
        
    }
}
