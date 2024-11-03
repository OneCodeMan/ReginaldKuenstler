//
//  MasterPaletteDetailView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-11-02.
//

import SwiftUI

struct MasterPaletteDetailView: View {
    let images = ["caravaggio0", "caravaggio1", "caravaggio2", "caravaggio3", "caravaggio4", "caravaggio5"]
    
    var body: some View {
        TabView {
            ForEach(images, id: \.self) { image in
                Image(image)
                    .resizable()
                    .scaledToFit()
                    .frame(width: UIScreen.main.bounds.width, height: UIScreen.main.bounds.height * 0.9) // Fill most of the screen
                    .clipped()
                    .padding(.bottom, 20)
            }
        }
        .tabViewStyle(PageTabViewStyle())
        .edgesIgnoringSafeArea(.all) // Makes images fill edge to edge
    }
}

#Preview {
    MasterPaletteDetailView()
}
