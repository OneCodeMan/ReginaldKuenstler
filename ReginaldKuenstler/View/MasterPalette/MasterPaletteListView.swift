//
//  MasterPalette.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-11-02.
//

import SwiftUI

struct MasterPaletteListView: View {
    var body: some View {
        NavigationStack {
            ScrollView {
                ForEach(MasterPaletteConstants.masterPalettes, id: \.self) { masterPalette in
                    NavigationLink(destination: MasterPaletteDetailView(images: masterPalette.imageStrings)) {
                        HStack {
                            Rectangle()
                                .fill(.orange)
                                .cornerRadius(4)
                                .frame(width: 30, height: 30)
                            VStack {
                                Text(masterPalette.artistName)
                                    .font(.defaultFontTitle)
                            }
                        }
                    } // ForEach
                }
            }
        } // end of Nav Stack
        .statusBar(hidden: true)
    }
}

#Preview {
    MasterPaletteListView()
}
