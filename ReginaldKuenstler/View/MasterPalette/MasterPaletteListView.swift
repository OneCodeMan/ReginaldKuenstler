//
//  MasterPalette.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-11-02.
//

import SwiftUI

struct MasterPaletteListView: View {
    
    @State var palettePreview: Palette = Palette.mockPalette

    var body: some View {
        NavigationStack {
            List(MasterPaletteConstants.masterPalettes, id: \.self) { masterPalette in
                NavigationLink(destination: MasterPaletteDetailView(masterPalette: masterPalette)) {
                    HStack(alignment: .top) {
                        Image(masterPalette.imageStrings[0])
                            .resizable()
                            .scaledToFit()
                            .cornerRadius(4)
                            .frame(width: 120, height: 90)
                            .padding(.trailing)
                        
                        VStack(alignment: .center) {
                            Text(masterPalette.artistName)
                                .font(.defaultFontTitle)
                            
                            HStack(alignment: .center) {
                                ForEach(Array(palettePreview.colours.prefix(upTo: 5)), id: \.self) { pc in
                                    SingularPaletteItemView(paletteColour: pc, circleHeight: 20, omitColourName: true)
                                }
                            }
                        }
                    } // HStack
                }
                .frame(maxHeight: 90, alignment: .top) // Enforce height limit to 70 and align top
                .background(
                    Image(masterPalette.imageStrings[1])
                        .resizable()
                        .scaledToFill() // Ensures the image fills the VStack
                        .edgesIgnoringSafeArea(.all)
                        .opacity(0.2)
                ) //Navlink
            }
            .navigationTitle(Text(String(localized: "Palette of the Greats")))
        } // end of Nav Stack
        .statusBar(hidden: true)
    }
}

#Preview {
    MasterPaletteListView()
}
