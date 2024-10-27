//
//  MessageView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-27.
//

import SwiftUI

struct MessageView: View {
    @State var fuckYouCount = 50
    var body: some View {
        ScrollView {
            VStack {
                Text("Dear User of my App,")
                    .font(.largeTitle)
                Text("I already know what your going to say. 'This app sucks'. 'This design sucks'")
                Text("The colour groups don't even have the proper colours...")
                Text("The colour classification is dog shit....")
                Text("a first year dumbass CS student could make a way better app.")
                Text("My reply to that is the following, and please read the entire thing.")
                
                ForEach(1...50, id: \.self) { _ in
                    Text("Fuck you.")
                }
            }

        }
    }
}

#Preview {
    MessageView()
}
