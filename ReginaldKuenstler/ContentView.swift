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
    
    // colours
    @State var colour1: UIColor = UIColor.red
    @State var colour2: UIColor = UIColor.red
    @State var colour3: UIColor = UIColor.red
    @State var colour4: UIColor = UIColor.red
    @State var colour5: UIColor = UIColor.red
    @State var colour6: UIColor = UIColor.red
    
    var body: some View {
        VStack {
            VStack {
                Image(uiImage: UIImage(named: "starz")!)
                    .resizable()
                    .frame(width: 200, height: 200)
                Text(infoString)
            }
            HStack {
                Rectangle()
                    .fill(Color(colour1))
                    .frame(width: 20, height: 20)
                Rectangle()
                    .fill(Color(colour2))
                    .frame(width: 20, height: 20)
                Rectangle()
                    .fill(Color(colour3))
                    .frame(width: 20, height: 20)
                Rectangle()
                    .fill(Color(colour4))
                    .frame(width: 20, height: 20)
                Rectangle()
                    .fill(Color(colour5))
                    .frame(width: 20, height: 20)
                Rectangle()
                    .fill(Color(colour6))
                    .frame(width: 20, height: 20)
            }
        }
        .padding()
        .onAppear {
            let vm = KuenstlerViewModel()
            self.imgTitle = "Calum from Aftersun"
            self.imgName = "starz"
            let image = UIImage(named: imgName)!
            let artwork = Artwork(image: image, title: imgTitle)
            vm.performAnalOnImage(artwork: artwork) { outputColours in
                DispatchQueue.main.async {
                    if outputColours.count == 6 {
                        self.colour1 = outputColours[0]
                        self.colour2 = outputColours[1]
                        self.colour3 = outputColours[2]
                        self.colour4 = outputColours[3]
                        self.colour5 = outputColours[4]
                        self.colour6 = outputColours[5]
                    } else {
                        print("outputColours has \(outputColours.count) items")
                    }
                }
            }
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
    
    func performAnalOnImage(artwork: Artwork, completion: @escaping ([UIColor]) -> Void) {
        var infoString = ""
        var uiColours: [UIColor] = []
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
                let outputCode = outputColour.rgbCode
                let currentColour = UIColor(red: CGFloat(outputCode.r) / 255.0, green: CGFloat(outputCode.g) / 255.0, blue: CGFloat(outputCode.b) / 255.0, alpha: 1.0)
                uiColours.append(currentColour)
                
                let yap = "Vibrant took the input as \(inputColour), which corresponds to \(outputColour.name) (hex code: \(outputColour.hexCode))\nThe UIColor for \(outputColour.name) is: \(currentColour)\n\n"
                infoString += yap
                print(yap)
            }
            print("printing uiColours within callback: \(uiColours)")
            completion(uiColours)
        }
    }
}
