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
