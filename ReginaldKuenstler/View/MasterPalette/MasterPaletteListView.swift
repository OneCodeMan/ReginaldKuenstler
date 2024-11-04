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
                NavigationLink(destination: MasterPaletteDetailView(images: masterPalette.imageStrings)) {
                    HStack {
                        Rectangle()
                            .fill(.orange)
                            .cornerRadius(4)
                            .frame(width: 70, height: 70)
                        VStack(alignment: .center) {
                            Text(masterPalette.artistName)
                                .font(.defaultFontTitle)
                            
                            HStack(alignment: .center) {
                                ForEach(Array(palettePreview.colours.prefix(upTo: 5)), id: \.self) { pc in
                                    SingularPaletteItemView(paletteColour: pc, circleHeight: 20, omitColourName: true)
                                }
                            }
                        }
                    }
                } // ForEach
            }
            .navigationTitle(Text(String(localized: "Palette of the Greats")))
        } // end of Nav Stack
        .statusBar(hidden: true)
    }
}

#Preview {
    MasterPaletteListView()
}
